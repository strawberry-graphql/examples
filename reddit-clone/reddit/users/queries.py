from typing import Optional

import strawberry
from strawberry.types import Info
from sqlalchemy import select

from reddit.database import get_session
from reddit.users.types import UserType
from reddit.users.models import User


@strawberry.type
class UserQuery:
    @strawberry.field(description="Gets an user by username.")
    async def user(self, info: Info, username: str) -> Optional[UserType]:
        query = select(User).filter_by(username=username).first()
        async with get_session() as session:
            user = await session.execute(query)
        if user is not None:
            return UserType.from_instance(user)

    @strawberry.field(description="Gets the current user.")
    async def current_user(self, info: Info) -> UserType:
        pass
