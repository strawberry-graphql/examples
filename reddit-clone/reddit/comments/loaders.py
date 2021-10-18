from typing import List, Optional, Dict

from sqlalchemy import select
from sqlalchemy.engine import Result

from reddit.database import get_session
from reddit.comments.models import Comment


async def load_comments_by_id(comment_ids: List[int]) -> List[Optional[Comment]]:
    """
    Batch-loads comments by their IDs.
    """
    query = select(Comment).filter(Comment.id.in_(comment_ids))
    async with get_session() as session:
        result: Result = await session.execute(query)
    comment_map: Dict[int, Comment] = {
        comment.id: comment for comment in result.scalars()
    }
    return [comment_map.get(comment_id) for comment_id in comment_ids]
