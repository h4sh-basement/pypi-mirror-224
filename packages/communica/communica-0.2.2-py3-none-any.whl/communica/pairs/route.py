import asyncio

from uuid import uuid4
from typing import TypedDict, Any, cast

from communica.utils import TaskSet, logger
from communica.exceptions import ReqError, RespError, SerializerError
from communica.serializers import BaseSerializer, default_serializer
from communica.connectors.base import (
    BaseConnection, BaseConnector,
    HandshakeOk, HandshakeFail, HandshakeGen
)

from communica.pairs.base import SyncHandlerType, AsyncHandlerType
from communica.pairs.simple import (
    ReqRepClient, ReqRepServer,
    RequestType, RequestHandler,
    ReqRepMessageFlow, ServerHandshakeOk
)


__all__ = (
    'RouteClient',
    'RouteServer'
)


class Metadata(TypedDict):
    id: str
    type: RequestType
    route: str


class RouteMessageFlow(ReqRepMessageFlow):
    __slots__ = ('routes', 'fallback_task_set', '_response_serializers',)

    routes: 'dict[str, tuple[RequestHandler, BaseSerializer]]'
    fallback_task_set: TaskSet

    _response_serializers: 'dict[str, BaseSerializer]'

    def __init__(self):
        super().__init__()
        self.routes = {}
        self.fallback_task_set = TaskSet()
        self._response_serializers = {}

    def update_route(
            self,
            route: str,
            handler: 'SyncHandlerType | AsyncHandlerType',
            serializer: 'BaseSerializer | None'
    ):
        if serializer is None:
            serializer = default_serializer
        self.routes[route] = (RequestHandler(handler), serializer)

    def dispatch(self, metadata: Metadata, raw_data: bytes):
        if metadata['type'] < RequestType.RESP_OK:
            try:
                route_handle = self.routes[metadata['route']]
                task_set = route_handle[0].running_tasks
            except KeyError:
                route_handle = None
                task_set = self.fallback_task_set

            task_set.create_task_with_exc_log(
                self.handle_request(route_handle, metadata, raw_data)
            )
        else:
            try:
                serializer = self._response_serializers[metadata['route']]
            except KeyError:  # pragma: no cover
                # this is possible after program restart.
                # just log and skip, cause we don't have a routine,
                # waiting for this response
                # XXX: should it be logged?
                logger.warning('Got response with not requested '
                              f'route ({metadata["route"]})')
                return
            self._handle_response(serializer, metadata, raw_data)

    async def handle_request(
            self,
            route_handle: 'tuple[RequestHandler, BaseSerializer] | None',
            req_meta: Metadata,
            raw_data: bytes
        ):
        if route_handle is not None:
            handler, serializer = route_handle
            resp_meta, resp_data = await self._handle_request(
                handler, serializer, req_meta, raw_data
            )
        else:
            serializer = default_serializer
            resp_meta = req_meta.copy()
            resp_meta['type'] = RequestType.RESP_ERR_REQUESTER
            resp_data = \
                ReqError(f'Route "{req_meta["route"]}" not exists').to_dict()

        await self._send_response(req_meta, resp_meta, resp_data, serializer)

    async def request(
            self,
            route: str,
            serializer: 'BaseSerializer | None',
            data: Any
    ) -> bytes:
        request_id, fut = self._create_response_waiter()

        serializer = serializer or default_serializer
        if (saved_serializer := self._response_serializers.get(route)) is None:
            self._response_serializers[route] = serializer
        elif saved_serializer is not serializer:
            raise TypeError('You should always use the same serializer for '
                           f'the same route ({saved_serializer!r} '
                            'has already been used earlier)')

        await self._connection.send(
            Metadata(id=request_id, type=RequestType.REQ_REP, route=route),
            serializer.client_dump(data)
        )

        return await fut

    async def throw(
            self,
            route: str,
            serializer: 'BaseSerializer | None',
            data: Any
    ) -> None:
        await self._connection.send(
            Metadata(id='', type=RequestType.REQ_THROW, route=route),
            (serializer or default_serializer).client_dump(data)
        )


class RouteClient(ReqRepClient):
    """
    Pair for RouteServer.

    Handler searched by exact match of route string.
    """

    __slots__ = ()

    _flow: RouteMessageFlow

    def __init__(
            self,
            connector: BaseConnector,
            client_id: 'str | None' = None
    ) -> None:
        super().__init__(connector)

        self._flow = RouteMessageFlow()

        self._run_task = None
        self._client_id = client_id or uuid4().hex

    def route_handler(
            self,
            route: str,
            serializer: 'BaseSerializer | None' = None
    ):
        """
        Register handler for route

        Args:
            route: Handler identifier.
            serializer: Defaults to JsonSerializer.
        """
        def decorator(endpoint: 'SyncHandlerType | AsyncHandlerType'):
            self._flow.update_route(route, endpoint, serializer)

        return decorator

    async def request(
            self,
            route: str,
            data: Any,
            serializer: 'BaseSerializer | None' = None
    ) -> Any:
        """
        Send request, wait response.

        Args:
            route: Handler identifier
            client_id: If omitted or None, random client will be chosen
        """
        return await self._flow.request(route, serializer, data)

    async def throw(
            self,
            route: str,
            data: Any,
            serializer: 'BaseSerializer | None' = None
    ) -> None:
        """
        Send request without waiting response.

        Args:
            route: Handler identifier
            client_id: If omitted or None, random client will be chosen
        """
        return await self._flow.throw(route, serializer, data)


class RouteServer(ReqRepServer):
    """
    Pair for RouteClient.

    Handler searched by exact match of route string.
    """

    __slots__ = ('_routes',)

    _known_clients: 'dict[str, RouteMessageFlow | asyncio.Future[RouteMessageFlow]]'

    def __init__(
            self,
            connector: BaseConnector,
    ) -> None:
        self.connector = connector
        self._routes = []
        self._known_clients = {}
        self._client_conn_runners = {}

    def route_handler(
            self,
            route: str,
            serializer: 'BaseSerializer | None' = None
    ):
        """
        Register handler for route

        Args:
            route: Handler identifier.
            serializer: Defaults to JsonSerializer.
        """
        def decorator(endpoint: 'SyncHandlerType | AsyncHandlerType'):
            for flow in self._known_clients.values():
                if isinstance(flow, RouteMessageFlow):
                    flow.update_route(route, endpoint, serializer)
            self._routes.append((route, endpoint, serializer))

        return decorator

    def _cancel_handler_tasks(self, flow: RouteMessageFlow):
        flow.fallback_task_set.cancel()

        for handler, _ in flow.routes.values():
            handler.running_tasks.cancel()

    def _on_client_connect(self, connection: BaseConnection):
        loop = self._get_loop()
        handshake_result = cast(ServerHandshakeOk, connection.get_handshake_result())
        client_id = handshake_result.client_id

        flow = self._known_clients.get(client_id)
        if not isinstance(flow, RouteMessageFlow):
            new_flow = RouteMessageFlow()
            for route, handler, serializer in self._routes:
                new_flow.update_route(route, handler, serializer)
            if isinstance(flow, asyncio.Future):
                flow.set_result(new_flow)
            self._known_clients[client_id] = new_flow
            flow = new_flow
        flow.update_connection(connection)

        task = loop.create_task(connection.run_until_fail(flow.dispatch))
        task.add_done_callback(self._on_conn_fail)
        self._client_conn_runners[client_id] = task

    async def request(
            self,
            route: str,
            data: Any,
            serializer: 'BaseSerializer | None' = None,
            client_id: 'str | None' = None
    ) -> Any:
        """
        Send request, wait response.

        Args:
            route: Handler identifier.
            client_id: If omitted or None, random connected client will be chosen.
            serializer: Defaults to JsonSerializer.
        """
        flow = await self._get_client_flow(client_id)
        return await flow.request(route, serializer, data)

    async def throw(
            self,
            route: str,
            data: Any,
            serializer: 'BaseSerializer | None' = None,
            client_id: 'str | None' = None
    ) -> None:
        """
        Send request without waiting response.

        Args:
            route: Handler identifier.
            client_id: If omitted or None, random connected client will be chosen.
            serializer: Defaults to JsonSerializer.
        """
        flow = await self._get_client_flow(client_id)
        return await flow.throw(route, serializer, data)
