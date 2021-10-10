from typing import Union

import strawberry
from strawberry.types import Info

from reddit.comments.types import CommentType


__all__ = ("comment_vote",)


@strawberry.input
class CommentVoteInput:
    comment_id: strawberry.ID
    subreddit_id: strawberry.ID
    post_id: strawberry.ID


@strawberry.type
class CommentVoteSuccess:
    comment: CommentType


@strawberry.type
class CommentVoteError:
    error: str


CommentVoteResult = Union[CommentVoteSuccess, CommentVoteError]


async def resolve_comment_vote(
    info: Info, input: CommentVoteInput
) -> CommentVoteResult:
    pass


comment_vote = strawberry.mutation(
    resolver=resolve_comment_vote,
    description="""
    Creates a vote on a comment.
    """,
)
