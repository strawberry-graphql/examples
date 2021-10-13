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
        The name of the Subreddit.
        """
    )

    description: str = strawberry.field(
        description="""
        The description of the Subreddit.
        """
    )

    admin_id: int = strawberry.field(
        description="""
        The owner ID of the Subreddit.
        """
    )

    submit_text: str = strawberry.field(
        description="""
        The text set by the Subreddit moderators, intended
        to be displayed on the submission form.
        """
    )

    icon: str = strawberry.field(
        description="""
        The icon URL of the Subreddit.
        """
    )

    posts: List[PostType] = strawberry.field(
        description="""
        The posts for the Subreddit.
        """
    )

    @classmethod
    async def resolve_node(
        cls, info: Info, subreddit_id: str
    ) -> Optional[SubredditType]:
        """
        Gets a Subreddit with the given ID.
        """
        query = select(Subreddit).filter_by(id=subreddit_id).first()
        async with get_session() as session:
            subreddit = await session.execute(query)
        if subreddit is not None:
            return cls.from_instance(subreddit)
