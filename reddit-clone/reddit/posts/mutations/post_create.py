from typing import Union, Optional

import strawberry
from strawberry.types import Info

from reddit.posts.types import PostType


__all__ = ("post_create",)


@strawberry.input
class PostCreateInput:
    title: str
    subreddit_id: strawberry.ID
    text: Optional[str]


@strawberry.type
class PostCreateSuccess:
    post: PostType


@strawberry.type
class PostCreateError:
    error: str


PostCreateResult = Union[PostCreateSuccess, PostCreateError]


@strawberry.mutation(description="Creates a new post in a subreddit.")
async def post_create(info: Info, input: PostCreateInput) -> PostCreateResult:
    pass
