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


async def resolve_subreddit_leave(
    info: Info, input: SubredditLeaveInput
) -> SubredditLeaveResult:
    pass


subreddit_leave = strawberry.mutation(
    resolver=resolve_subreddit_leave,
    description="""
    Deletes a Subreddit-User relationship.
    """,
)
