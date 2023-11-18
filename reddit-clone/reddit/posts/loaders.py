from typing import List, Optional, Dict

from sqlalchemy import select
from sqlalchemy.engine import Result

from reddit.database import get_session
from reddit.posts.models import Post


async def load_posts_by_id(post_ids: List[int]) -> List[Optional[Post]]:
    """
    Batch-loads posts by their IDs.
    """
    query = select(Post).filter(Post.id.in_(post_ids))
    async with get_session() as session:
        result: Result = await session.execute(query)
    post_map: Dict[int, Post] = {post.id: post for post in result.scalars()}
    return [post_map.get(post_id) for post_id in post_ids]
