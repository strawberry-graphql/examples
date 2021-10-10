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


async def resolve_subreddit_join(
    info: Info, input: SubredditJoinInput
) -> SubredditJoinResult:
    pass


subreddit_join = strawberry.mutation(
    name="subreddit_join",
    resolver=resolve_subreddit_join,
    description="""
    Creates a new Subreddit-User relationship.
    """,
)
