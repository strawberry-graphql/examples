from fastapi import FastAPI
from strawberry.asgi import GraphQL

from reddit.core.config import DEBUG
from reddit.schema import schema

__all__ = ("app",)


def create_application() -> FastAPI:
    """
    Creates an application instance.

    :return: The created application.
    """
    application = FastAPI(title="Reddit GraphQL", debug=DEBUG)

    application.add_route(
        path="/graphql", route=GraphQL(schema=schema, graphiql=True, debug=DEBUG)
    )

    return application


app = create_application()
