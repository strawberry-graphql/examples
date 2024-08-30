from typing import Union

import strawberry
from strawberry.types import Info

from reddit.users.types import UserType

__all__ = ("avatar_remove",)


@strawberry.type
class AvatarRemoveSuccess:
    user: UserType


@strawberry.type
class AvatarRemoveError:
    error: str


AvatarRemoveResult = Union[AvatarRemoveSuccess, AvatarRemoveError]


@strawberry.mutation(description="Removes the current user's avatar.")
async def avatar_remove(info: Info) -> AvatarRemoveResult:
    pass
