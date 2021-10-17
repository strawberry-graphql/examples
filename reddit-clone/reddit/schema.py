from strawberry import Schema
from strawberry.tools import merge_types

from reddit.base.queries import BaseQuery
from reddit.subreddits.queries import SubredditQuery
from reddit.users.queries import UserQuery
from reddit.comments.mutations import CommentMutation
from reddit.posts.mutations import PostMutation
from reddit.subreddits.mutations import SubredditMutation
from reddit.users.mutations import UserMutation

__all__ = ("schema",)

Query = merge_types(name="Query", types=(BaseQuery, UserQuery, SubredditQuery))

Mutation = merge_types(
    name="Mutation",
    types=(CommentMutation, PostMutation, UserMutation, SubredditMutation),
)


schema = Schema(query=Query, mutation=Mutation)
