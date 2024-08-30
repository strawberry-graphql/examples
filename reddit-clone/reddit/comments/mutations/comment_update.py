from typing import Union, Optional

import strawberry
from strawberry.types import Info

from reddit.comments.types import CommentType


__all__ = ("comment_update",)


@strawberry.input
class CommentUpdateInput:
    comment: Optional[str]
    comment_id: strawberry.ID
    subreddit_id: strawberry.ID
    post_id: strawberry.ID


@strawberry.type
class CommentUpdateSuccess:
    comment: CommentType


@strawberry.type
class CommentUpdateError:
    error: str


CommentUpdateResult = Union[CommentUpdateSuccess, CommentUpdateError]


@strawberry.field(description="Updates a comment on a post.")
async def comment_update(info: Info, input: CommentUpdateInput) -> CommentUpdateResult:
    pass
