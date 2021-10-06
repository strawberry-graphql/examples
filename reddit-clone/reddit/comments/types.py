from __future__ import annotations

from typing import List, Optional

from strawberry import type, field
from strawberry.types import Info
from sqlalchemy import select

from reddit.base.types import NodeType
from reddit.comments.models import Comment
from reddit.database import get_session


@type(name="Comment")
class CommentType(NodeType):
    content: str = field(
        description="""
        The content of the comment.
        """
    )

    votes: int = field(
        description="""
        The votes the comment has.
        """
    )

    user_id: Optional[int] = field(
        description="""
        The owner ID of the comment.
        """
    )

    replies: List[CommentType] = field(
        description="""
        The replies for the comment.
        """
    )

    @classmethod
    async def resolve_node(cls, info: Info, comment_id: str) -> Optional[CommentType]:
        """
        Gets a comment with the given ID.
        """
        query = select(Comment).filter_by(id=comment_id).first()
        async with get_session() as session:
            comment = await session.execute(query)
        if comment is not None:
            return cls.from_instance(comment)

    @classmethod
    def from_instance(cls, instance: Comment) -> CommentType:
        return CommentType(
            id=instance.id,
            content=instance.content,
            votes=instance.votes,
            user_id=instance.user_id,
            replies=instance.replies,
        )
