from typing import List

import strawberry
from strawberry.tools import create_type
from strawberry.types import Info

from reddit.subreddits.types import SubredditType


async def resolve_subreddits(info: Info) -> List[SubredditType]:
    pass


subreddits = strawberry.field(
    name="subreddits",
    resolver=resolve_subreddits,
    description="""
    Gets the available subreddits.
    """,
)

SubredditQuery = create_type(name="SubredditQuery", fields=(subreddits,))
