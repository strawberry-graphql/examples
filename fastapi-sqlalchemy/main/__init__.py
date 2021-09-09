from fastapi import FastAPI
from strawberry.asgi import GraphQL

from api.schema import schema

graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
