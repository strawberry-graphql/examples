from __future__ import annotations

from typing import List, Optional

from strawberry import type, field

from reddit.users.models import User
from reddit.base.types import NodeType
from reddit.posts.types import PostType
from reddit.subreddits.types import SubredditType
from reddit.comments.types import CommentType


@type(name="User")
class UserType(NodeType):
    username: str = field(
        description="""
        The username of the user.
        """
    )

    avatar: Optional[str] = field(
        description="""
        The avatar URL of the user.
        """
    )

    posts: List[PostType] = field(
        description="""
        The posts for the user.
        """
    )

    subreddits: List[SubredditType] = field(
        description="""
        The subreddits the user is in.
        """
    )

    comments: List[CommentType] = field(
        description="""
        The comments for the user.
        """
    )

    @classmethod
    def from_instance(cls, instance: User) -> UserType:
        return UserType(
            id=instance.id,
            username=instance.username,
            avatar=instance.avatar,
            posts=instance.posts,
            subreddits=instance.subreddits,
            comments=instance.comments,
        )
