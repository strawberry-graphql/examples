import strawberry

from reddit.base.queries import BaseQuery
from reddit.subreddits.queries import SubredditQuery
from reddit.users.queries import UserQuery
from reddit.subreddits.mutations import SubredditMutation
from reddit.users.mutations import UserMutation


@strawberry.type
class Query(BaseQuery, UserQuery, SubredditQuery):
    pass


@strawberry.type
class Mutation(UserMutation, SubredditMutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
