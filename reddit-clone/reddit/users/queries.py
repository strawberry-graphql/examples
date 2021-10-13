from typing import Optional, cast

import strawberry
from strawberry.tools import create_type
from strawberry.types import Info

from reddit.database import get_session
from reddit.users.types import UserType
from reddit.users.models import User


async def resolve_user(info: Info, username: str) -> Optional[UserType]:
    async with get_session() as session:
        user = await User.by_username(session=session, username=username)
    if user is not None:
        return cast(UserType, user)
    return user


user = strawberry.field(
    resolver=resolve_user,
    description="""
    Gets an user by username.
    """,
)


async def resolve_current_user(info: Info) -> Optional[UserType]:
    pass


current_user = strawberry.field(
    resolver=resolve_current_user,
    description="""
    Gets the current user.
    """,
)

UserQuery = create_type(name="UserQuery", fields=(user, current_user))
