import strawberry

from reddit.base.queries import BaseQueries


@strawberry.type
class Query(BaseQueries):
    pass


schema = strawberry.Schema(query=Query)
