from __future__ import annotations

from typing import List, Optional, cast

import strawberry
from strawberry.types import Info

from reddit.base.types import NodeType
from reddit.comments.types import CommentType


@strawberry.type(name="Post")
class PostType(NodeType):
    title: str = strawberry.field(
        description="""
        The title of the post.
        """
    )

    text: Optional[str] = strawberry.field(
        description="""
        The text for the post.
        """
    )

    link: Optional[str] = strawberry.field(
        description="""
        The link of the post.
        """
    )

    thumbnail: Optional[str] = strawberry.field(
        description="""
        The thumbnail URL of the post.
        """
    )

    owner_id: int = strawberry.field(
        description="""
        The owner ID of the post.
        """
    )

    subreddit_id: int = strawberry.field(
        description="""
        The subreddit ID of the post.
        """
    )

    votes: int = strawberry.field(
        description="""
        The votes the post has.
        """
    )

    comments: List[CommentType] = strawberry.field(
        description="""
        The comments for the post.
        """
    )

    @classmethod
    async def resolve_node(cls, info: Info, post_id: str) -> Optional[PostType]:
        """
        Gets a post with the given ID.
        """
        loader = info.context.get("post_loader")
        post = await loader.load(post_id)
        return cast(PostType, post)
