from strawberry import type, Schema

from reddit.base.queries import BaseQueries


@type
class Query(BaseQueries):
    pass


schema = Schema(query=Query)
