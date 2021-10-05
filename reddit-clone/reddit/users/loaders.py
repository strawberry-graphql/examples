from typing import List, Optional, Dict

from sqlalchemy import select
from sqlalchemy.engine import Result

from reddit.database import get_session
from reddit.users.models import User


async def load_users(user_ids: List[int]) -> List[Optional[User]]:
    """
    Batch-loads users by their IDs.
    """
    query = select(User).filter(User.id.in_(user_ids))
    async with get_session() as session:
        result: Result = await session.execute(query)
    user_map: Dict[int, User] = {user.id: user for user in result.scalars()}
    return [user_map.get(user_id) for user_id in user_ids]
