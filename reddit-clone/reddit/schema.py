from strawberry import type, field, Schema


@type
class Query:
    @field
    def hello_world(self) -> str:
        return "Hello world!"


schema = Schema(query=Query, mutation=None)
