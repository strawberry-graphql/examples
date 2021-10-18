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


@strawberry.mutation(description="Deletes a subreddit.")
async def subreddit_delete(
    info: Info, input: SubredditDeleteInput
) -> SubredditDeleteResult:
    pass
