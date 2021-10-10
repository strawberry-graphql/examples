from typing import Optional

import strawberry
from strawberry.tools import create_type
from strawberry.types import Info

from reddit.users.types import UserType


async def resolve_user(info: Info, username: str) -> Optional[UserType]:
    pass


user = strawberry.field(
    name="user",
    resolver=resolve_user,
    description="""
    Gets an user by username.
    """,
)


async def resolve_current_user(info: Info) -> UserType:
    pass


current_user = strawberry.field(
    name="current_user",
    resolver=resolve_current_user,
    description="""
    Gets the current user.
    """,
)

UserQuery = create_type(name="UserQuery", fields=(user, current_user))
