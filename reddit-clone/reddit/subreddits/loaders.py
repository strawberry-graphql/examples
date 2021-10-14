from typing import List, Optional, Dict

from sqlalchemy import select
from sqlalchemy.engine import Result

from reddit.database import get_session
from reddit.subreddits.models import Subreddit


async def load_subreddits(subreddit_ids: List[int]) -> List[Optional[Subreddit]]:
    """
    Batch-loads subreddits by their IDs.
    """
    query = select(Subreddit).filter(Subreddit.id.in_(subreddit_ids))
    async with get_session() as session:
        result: Result = await session.execute(query)
    subreddit_map: Dict[int, Subreddit] = {
        subreddit.id: subreddit for subreddit in result.scalars()
    }
    return [subreddit_map.get(subreddit_id) for subreddit_id in subreddit_ids]
