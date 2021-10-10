from typing import Union

import strawberry
from strawberry.types import Info

from reddit.comments.types import CommentType


__all__ = ("comment_delete",)


@strawberry.input
class CommentDeleteInput:
    comment_id: strawberry.ID
    subreddit_id: strawberry.ID
    post_id: strawberry.ID


@strawberry.type
class CommentDeleteSuccess:
    comment: CommentType


@strawberry.type
class CommentDeleteError:
    error: str


CommentDeleteResult = Union[CommentDeleteSuccess, CommentDeleteError]


async def resolve_comment_delete(
    info: Info, input: CommentDeleteInput
) -> CommentDeleteResult:
    pass


comment_delete = strawberry.mutation(
    name="comment_delete",
    resolver=resolve_comment_delete,
    description="""
    Deletes a comment on a post.
    """,
)
