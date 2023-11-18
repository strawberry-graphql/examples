from strawberry.asgi import GraphQL

from api.schema import schema

app = GraphQL(schema)
