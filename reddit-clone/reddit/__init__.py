from typing import Union, Optional, Any

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response
from starlette.websockets import WebSocket
from strawberry.dataloader import DataLoader
from strawberry.asgi import GraphQL

from reddit import settings
from reddit.schema import schema
from reddit.users.loaders import load_users

__all__ = ("app",)


class MyGraphQL(GraphQL):
    async def get_context(
        self, request: Union[Request, WebSocket], response: Optional[Response] = None
    ) -> Optional[Any]:
        context: dict = await super().get_context(request, response=response)
        context.update(user_loader=DataLoader(load_fn=load_users))
        return context


def create_application() -> Starlette:
    """
    Creates an application instance.

    :return: The created application.
    """
    app = Starlette(debug=settings.DEBUG)
    app.add_route(
        path="/graphql",
        route=GraphQL(schema=schema, graphiql=True, debug=settings.DEBUG),
    )

    return app


app = create_application()
