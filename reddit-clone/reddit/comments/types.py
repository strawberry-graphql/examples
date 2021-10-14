from __future__ import annotations

from typing import List, Optional, cast

import strawberry
from strawberry.types import Info

from reddit.base.types import NodeType


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

    owner_id: Optional[int] = strawberry.field(
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
        loader = info.context.get("comment_loader")
        comment = await loader.load(comment_id)
        return cast(CommentType, comment)
