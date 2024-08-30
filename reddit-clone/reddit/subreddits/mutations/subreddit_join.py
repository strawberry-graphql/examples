from typing import Union

import strawberry
from strawberry.types import Info

from reddit.subreddits.types import SubredditType


__all__ = ("subreddit_join",)


@strawberry.input
class SubredditJoinInput:
    subreddit_id: strawberry.ID


@strawberry.type
class SubredditJoinSuccess:
    subreddit: SubredditType


@strawberry.type
class SubredditJoinError:
    error: str


SubredditJoinResult = Union[SubredditJoinSuccess, SubredditJoinError]


@strawberry.mutation(
    description="""
    Creates a new subreddit-user relationship.
    """
)
async def subreddit_join(info: Info, input: SubredditJoinInput) -> SubredditJoinResult:
    pass
