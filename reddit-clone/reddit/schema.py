import strawberry


@strawberry.type
class Query:
    @strawberry.field()
    def hello_world(self) -> str:
        return "Hello world!"


schema = strawberry.Schema(query=Query, mutation=None)
