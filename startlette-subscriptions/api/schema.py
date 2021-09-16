import strawberry

from .subscription import Subscription


@strawberry.type
class Query:
    @strawberry.field
    def ping(self) -> str:
        return "pong"


schema = strawberry.Schema(Query, subscription=Subscription)
