from __future__ import annotations

from typing import List, Optional

import strawberry
from strawberry.types import Info
from sqlalchemy import select

from reddit.base.types import NodeType
from reddit.comments.models import Comment
from reddit.database import get_session


@strawberry.type(name="Comment")
class CommentType(NodeType):
    content: str = strawberry.field(
        description="""
        The content of the comment.
        """
    )

    votes: int = strawberry.field(
        description="""
        The votes the comment has.
        """
    )

    user_id: Optional[int] = strawberry.field(
        description="""
        The owner ID of the comment.
        """
    )

    replies: List[CommentType] = strawberry.field(
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
        pass
