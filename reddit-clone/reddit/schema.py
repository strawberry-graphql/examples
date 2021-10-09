import strawberry

from reddit.base.queries import BaseQuery
from reddit.users.queries import UserQuery
from reddit.users.mutations import UserMutation


@strawberry.type
class Query(BaseQuery, UserQuery):
    pass


@strawberry.type
class Mutation(UserMutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
