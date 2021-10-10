from typing import Optional, Union

import strawberry
from strawberry.types import Info

from reddit.subreddits.types import SubredditType


__all__ = ("subreddit_update",)


@strawberry.input
class SubredditUpdateInput:
    name: Optional[str]
    description: Optional[str]
    subreddit_id: strawberry.ID


@strawberry.type
class SubredditUpdateSuccess:
    subreddit: SubredditType


@strawberry.type
class SubredditUpdateError:
    error: str


SubredditUpdateResult = Union[SubredditUpdateSuccess, SubredditUpdateError]


async def resolve_subreddit_update(
    info: Info, input: SubredditUpdateInput
) -> SubredditUpdateResult:
    pass


subreddit_update = strawberry.mutation(
    resolver=resolve_subreddit_update,
    description="""
    Updates a Subreddit.
    """,
)
