from __future__ import annotations

from typing import List, Optional, cast

import strawberry
from strawberry.types import Info

from reddit.users.services import user_by_id
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
        async with get_session() as session:
            user = await user_by_id(session=session, id=user_id)
        if user is not None:
            return cast(UserType, user)
