import strawberry
from strawberry.types import Info


@strawberry.type
class UserMutations:
    @strawberry.mutation(description="Logs the current user out.")
    async def unauthenticate(self, info: Info, *args):
        pass
