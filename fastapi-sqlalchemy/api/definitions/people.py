import strawberry

from main.models import Person as PersonModel


@strawberry.type
class Person:
    id: int
    name: str

    instance: strawberry.Private[PersonModel]

    @classmethod
    def from_instance(cls, instance: PersonModel):
        return cls(
            instance=instance,
            id=instance.id,
            name=instance.name,
        )
