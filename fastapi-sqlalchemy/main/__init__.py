from fastapi import FastAPI
from strawberry.asgi import GraphQL

from api.schema import schema

graphql_app = GraphQL(schema)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.mount("/graphql", graphql_app)
