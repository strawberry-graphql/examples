from typing import Union

import strawberry
from strawberry.types import Info

from reddit.subreddits.types import SubredditType


__all__ = ("subreddit_delete",)


@strawberry.input
class SubredditDeleteInput:
    subreddit_id: strawberry.ID


@strawberry.type
class SubredditDeleteSuccess:
    subreddit: SubredditType


@strawberry.type
class SubredditDeleteError:
    error: str


SubredditDeleteResult = Union[SubredditDeleteSuccess, SubredditDeleteError]


async def resolve_subreddit_delete(
    info: Info, input: SubredditDeleteInput
) -> SubredditDeleteResult:
    pass


subreddit_delete = strawberry.mutation(
    name="subreddit_delete",
    resolver=resolve_subreddit_delete,
    description="""
    Deletes a Subreddit.
    """,
)
