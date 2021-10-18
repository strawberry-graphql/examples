from typing import Optional, cast

import strawberry
from strawberry.tools import create_type
from strawberry.types import Info

from reddit.users.types import UserType


@strawberry.field(description="Gets an user by username.")
async def user(info: Info, username: str) -> Optional[UserType]:
    loader = info.context.get("user_username_loader")
    user = await loader.load(username)
    return cast(UserType, user)


@strawberry.field(description="Gets the current user.")
async def current_user(info: Info) -> Optional[UserType]:
    pass


UserQuery = create_type(name="UserQuery", fields=(user, current_user))
