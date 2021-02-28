import typing

from starlette.requests import Request
from starlette.websockets import WebSocket
from strawberry.asgi import GraphQL

from .context import Context, get_broadcast


class MyGraphQL(GraphQL):
    async def get_context(
        self, request: typing.Union[Request, WebSocket]
    ) -> typing.Optional[typing.Any]:
        broadcast = await get_broadcast()

        return Context(broadcast)
