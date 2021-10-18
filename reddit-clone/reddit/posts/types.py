from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional, cast

import strawberry
from strawberry.types import Info
from strawberry.lazy_type import LazyType

from reddit.base.types import NodeType
from reddit.comments.types import CommentType

if TYPE_CHECKING:
    from reddit.subreddits.types import SubredditType
    from reddit.users.types import UserType


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

    @strawberry.field(description="The owner of the post.")
    async def owner(
        self, info: Info
    ) -> LazyType["UserType", "reddit.users.types"]:  # noqa: F821
        loader = info.context.get("user_id_loader")
        user = await loader.load(self.owner_id)
        return cast(UserType, user)

    @strawberry.field(description="The Subreddit of the post.")
    async def subreddit(
        self, info: Info
    ) -> LazyType["SubredditType", "reddit.subreddits.types"]:  # noqa: F821
        loader = info.context.get("subreddit_id_loader")
        subreddit = await loader.load(self.subreddit_id)
        return cast(SubredditType, subreddit)

    @classmethod
    async def resolve_node(cls, info: Info, post_id: str) -> Optional[PostType]:
        """
        Gets a post with the given ID.
        """
        loader = info.context.get("post_id_loader")
        post = await loader.load(post_id)
        return cast(PostType, post)
