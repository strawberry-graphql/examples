from typing import Optional, Union

import strawberry
from strawberry.types import Info

from reddit.subreddits.types import SubredditType


__all__ = ("subreddit_create",)


@strawberry.input
class SubredditCreateInput:
    name: str
    description: Optional[str]


@strawberry.type
class SubredditCreateSuccess:
    subreddit: SubredditType


@strawberry.type
class SubredditCreateError:
    error: str


SubredditCreateResult = Union[SubredditCreateSuccess, SubredditCreateError]


async def resolve_subreddit_create(
    info: Info, input: SubredditCreateInput
) -> SubredditCreateResult:
    pass


subreddit_create = strawberry.mutation(
    name="subreddit_create",
    resolver=resolve_subreddit_create,
    description="""
    Creates a new Subreddit.
    """,
)
