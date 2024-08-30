from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, cast

import strawberry
from strawberry.types import Info
from strawberry.lazy_type import LazyType

from reddit.base.types import NodeType

if TYPE_CHECKING:
    from reddit.users.types import UserType
    from reddit.posts.types import PostType


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

    post_id: int = strawberry.field(
        description="""
        The post ID of the comment.
        """
    )

    replies: List[CommentType] = strawberry.field(
        description="""
        The replies for the comment.
        """
    )

    @strawberry.field(description="The owner of the comment.")
    async def owner(
        self, info: Info
    ) -> LazyType["UserType", "reddit.users.types"]:  # noqa: F821
        loader = info.context.get("user_id_loader")
        user = await loader.load(self.owner_id)
        return cast(UserType, user)

    @strawberry.field(description="The post of the comment.")
    async def post(
        self, info: Info
    ) -> LazyType["PostType", "reddit.posts.types"]:  # noqa: F821
        loader = info.context.get("post_id_loader")
        post = await loader.load(self.post_id)
        return cast(PostType, post)

    @classmethod
    async def resolve_node(cls, info: Info, comment_id: str) -> Optional[CommentType]:
        """
        Gets a comment with the given ID.
        """
        loader = info.context.get("comment_id_loader")
        comment = await loader.load(comment_id)
        return cast(CommentType, comment)
