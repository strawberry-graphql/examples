from typing import Union

import strawberry
from strawberry.types import Info

from reddit.posts.types import PostType


__all__ = ("post_delete",)


@strawberry.input
class PostDeleteInput:
    post_id: strawberry.ID
    subreddit_id: strawberry.ID


@strawberry.type
class PostDeleteSuccess:
    post: PostType


@strawberry.type
class PostDeleteError:
    error: str


PostDeleteResult = Union[PostDeleteSuccess, PostDeleteError]


async def resolve_post_delete(info: Info, input: PostDeleteInput) -> PostDeleteResult:
    pass


post_delete = strawberry.mutation(
    name="post_delete",
    resolver=resolve_post_delete,
    description="""
    Deletes a post in a Subreddit.
    """,
)
