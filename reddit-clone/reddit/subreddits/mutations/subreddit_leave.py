from typing import Union

import strawberry
from strawberry.types import Info

from reddit.subreddits.types import SubredditType


__all__ = ("subreddit_leave",)


@strawberry.input
class SubredditLeaveInput:
    subreddit_id: strawberry.ID


@strawberry.type
class SubredditLeaveSuccess:
    subreddit: SubredditType


@strawberry.type
class SubredditLeaveError:
    error: str


SubredditLeaveResult = Union[SubredditLeaveSuccess, SubredditLeaveError]


@strawberry.field(
    description="""
    Deletes a subreddit-user relationship.
    """
)
async def subreddit_leave(
    info: Info, input: SubredditLeaveInput
) -> SubredditLeaveResult:
    pass
