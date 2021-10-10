import strawberry

from reddit.base.queries import BaseQuery
from reddit.subreddits.queries import SubredditQuery
from reddit.users.queries import UserQuery
from reddit.comments.mutations import CommentMutation
from reddit.posts.mutations import PostMutation
from reddit.subreddits.mutations import SubredditMutation
from reddit.users.mutations import UserMutation

__all__ = ("schema",)


@strawberry.type
class Query(BaseQuery, UserQuery, SubredditQuery):
    pass


@strawberry.type
class Mutation(CommentMutation, PostMutation, UserMutation, SubredditMutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
