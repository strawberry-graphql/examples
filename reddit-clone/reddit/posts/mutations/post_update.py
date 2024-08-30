from typing import Union, Optional

import strawberry
from strawberry.types import Info

from reddit.posts.types import PostType


__all__ = ("post_update",)


@strawberry.input
class PostUpdateInput:
    title: Optional[str]
    text: Optional[str]
    post_id: strawberry.ID
    subreddit_id: strawberry.ID


@strawberry.type
class PostUpdateSuccess:
    post: PostType


@strawberry.type
class PostUpdateError:
    error: str


PostUpdateResult = Union[PostUpdateSuccess, PostUpdateError]


@strawberry.mutation(description="Updates a post in a subreddit.")
async def post_update(info: Info, input: PostUpdateInput) -> PostUpdateResult:
    pass
