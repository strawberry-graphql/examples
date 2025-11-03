import strawberry

from main.models import User as UserModel


@strawberry.type
class User:
    id: int
    email: str

    @classmethod
    def from_instance(cls, instance: UserModel):
        return cls(
            id=instance.id,
            email=instance.email,
        )
