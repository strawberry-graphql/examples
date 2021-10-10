from typing import Union

import strawberry
from strawberry.types import Info

from reddit.posts.types import PostType


__all__ = ("post_vote",)


@strawberry.input
class PostVoteInput:
    post_id: strawberry.ID
    subreddit_id: strawberry.ID


@strawberry.type
class PostVoteSuccess:
    post: PostType


@strawberry.type
class PostVoteError:
    error: str


PostVoteResult = Union[PostVoteSuccess, PostVoteError]


async def resolve_post_vote(info: Info, input: PostVoteInput) -> PostVoteResult:
    pass


post_vote = strawberry.mutation(
    resolver=resolve_post_vote,
    description="""
    Creates a vote on a post.
    """,
)