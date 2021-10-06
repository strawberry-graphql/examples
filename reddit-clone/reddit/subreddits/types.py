from __future__ import annotations

from typing import List, Optional

import strawberry
from strawberry.types import Info
from sqlalchemy import select

from reddit.base.types import NodeType
from reddit.subreddits.models import Subreddit
from reddit.posts.types import PostType
from reddit.database import get_session


@strawberry.type(name="Subreddit")
class SubredditType(NodeType):
    name: str = strawberry.field(
        description="""
        The name of the subreddit.
        """
    )

    description: str = strawberry.field(
        description="""
        The description of the subreddit.
        """
    )

    admin_id: int = strawberry.field(
        description="""
        The owner ID of the subreddit.
        """
    )

    # TODO: make status an enum
    status: int = strawberry.field(
        description="""
        The status of the subreddit.
        """
    )

    icon: str = strawberry.field(
        description="""
        The icon URL of the subreddit.
        """
    )

    posts: List[PostType] = strawberry.field(
        description="""
        The posts for the subreddit.
        """
    )

    @classmethod
    async def resolve_node(
        cls, info: Info, subreddit_id: str
    ) -> Optional[SubredditType]:
        """
        Gets a subreddit with the given ID.
        """
        query = select(Subreddit).filter_by(id=subreddit_id).first()
        async with get_session() as session:
            subreddit = await session.execute(query)
        if subreddit is not None:
            return cls.from_instance(subreddit)

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
