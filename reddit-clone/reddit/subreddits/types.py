from __future__ import annotations

from typing import List, Optional

from strawberry import type, field
from strawberry.types import Info
from sqlalchemy import select

from reddit.base.types import NodeType
from reddit.subreddits.models import Subreddit
from reddit.posts.types import PostType
from reddit.database import get_session


@type(name="Subreddit")
class SubredditType(NodeType):
    name: str = field(
        description="""
        The name of the subreddit.
        """
    )

    description: str = field(
        description="""
        The description of the subreddit.
        """
    )

    admin_id: int = field(
        description="""
        The owner ID of the subreddit.
        """
    )

    # TODO: make status an enum
    status: int = field(
        description="""
        The status of the subreddit.
        """
    )

    icon: str = field(
        description="""
        The icon URL of the subreddit.
        """
    )

    posts: List[PostType] = field(
        description="""
        The posts for the subreddit.
        """
    )

    @classmethod
    async def get_node(cls, info: Info, subreddit_id: str) -> Optional[Subreddit]:
        """
        Gets a subreddit with the given ID.
        """
        query = select(Subreddit).filter_by(id=subreddit_id).first()
        async with get_session() as session:
            user = await session.execute(query)
        return user

    @classmethod
    def from_instance(cls, instance: Subreddit) -> SubredditType:
        return SubredditType(
            id=instance.id,
            description=instance.description,
            admin_id=instance.admin_id,
            status=instance.status,
            icon=instance.icon,
            posts=instance.posts,
        )
