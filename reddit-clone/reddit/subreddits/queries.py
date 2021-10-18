from typing import List

import strawberry
from strawberry.tools import create_type
from strawberry.types import Info

from reddit.subreddits.types import SubredditType


@strawberry.field(description="Gets the available subreddits.")
async def subreddits(info: Info) -> List[SubredditType]:
    pass


SubredditQuery = create_type(name="SubredditQuery", fields=(subreddits,))
