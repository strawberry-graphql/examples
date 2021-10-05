from typing import Union, Optional, Any

from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response
from starlette.websockets import WebSocket
from strawberry.dataloader import DataLoader
from strawberry.asgi import GraphQL

from reddit.settings import DEBUG
from reddit.schema import schema
from reddit.users.loaders import load_users


class MyGraphQL(GraphQL):
    async def get_context(
        self, request: Union[Request, WebSocket], response: Optional[Response] = None
    ) -> Optional[Any]:
        context: dict = await super().get_context(request, response=response)
        context.update(user_loader=DataLoader(load_fn=load_users))
        return context


def create_application() -> FastAPI:
    """
    Creates an application instance.

    :return: The created application.
    """
    application = FastAPI(title="Reddit GraphQL", debug=DEBUG)

    graphql_app = MyGraphQL(schema=schema, graphiql=True, debug=DEBUG)

    application.add_route(path="/graphql", route=graphql_app)

    return application


app = create_application()
