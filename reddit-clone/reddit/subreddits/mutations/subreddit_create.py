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


@strawberry.mutation(description="Creates a new subreddit.")
async def subreddit_create(
    info: Info, input: SubredditCreateInput
) -> SubredditCreateResult:
    pass
