from typing import Union

import strawberry
from strawberry.types import Info

from reddit.comments.types import CommentType


__all__ = ("comment_create",)


@strawberry.input
class CommentCreateInput:
    content: str
    subreddit_id: strawberry.ID
    post_id: strawberry.ID


@strawberry.type
class CommentCreateSuccess:
    comment: CommentType


@strawberry.type
class CommentCreateError:
    error: str


CommentCreateResult = Union[CommentCreateSuccess, CommentCreateError]


@strawberry.field(description="Creates a new comment on a post.")
async def comment_create(info: Info, input: CommentCreateInput) -> CommentCreateResult:
    pass
