from fastapi import FastAPI
from strawberry.asgi import GraphQL
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware.sessions import SessionMiddleware

from api.schema import schema

from .middleware import SessionBackend


middleware = [
    Middleware(SessionMiddleware, secret_key="supersecretkey"),
    Middleware(AuthenticationMiddleware, backend=SessionBackend()),
]

graphql_app = GraphQL(schema)

app = FastAPI(middleware=middleware)
app.mount("/graphql", graphql_app)
