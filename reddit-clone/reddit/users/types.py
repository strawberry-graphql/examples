from __future__ import annotations

from typing import List, Optional

import strawberry
from strawberry.types import Info
from sqlalchemy import select

from reddit.users.models import User
from reddit.base.types import NodeType
from reddit.posts.types import PostType
from reddit.subreddits.types import SubredditType
from reddit.comments.types import CommentType
from reddit.database import get_session


@strawberry.type(name="User")
class UserType(NodeType):
    username: str = strawberry.field(
        description="""
        The username of the user.
        """
    )

    avatar: str = strawberry.field(
        description="""
        The avatar URL of the user.
        """
    )

    posts: List[PostType] = strawberry.field(
        description="""
        The posts for the user.
        """
    )

    subreddits: List[SubredditType] = strawberry.field(
        description="""
        The subreddits the user is in.
        """
    )

    comments: List[CommentType] = strawberry.field(
        description="""
        The comments for the user.
        """
    )

    @classmethod
    async def resolve_node(cls, info: Info, user_id: str) -> Optional[UserType]:
        """
        Gets an user with the given ID.
        """
        query = select(User).filter_by(id=user_id).first()
        async with get_session() as session:
            user = await session.execute(query)
        if user is not None:
            return cls.from_instance(user)

    @classmethod
    def from_instance(cls, instance: User) -> UserType:
        pass
