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

    graphql_app = GraphQL(schema=schema, graphiql=True, debug=DEBUG)

    application.add_route(path="/graphql", route=graphql_app)

    return application


app = create_application()
