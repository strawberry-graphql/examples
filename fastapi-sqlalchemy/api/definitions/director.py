import strawberry

from main.models import Director as DirectorModel


@strawberry.type
class Director:
    id: int
    name: str

    @classmethod
    def from_instance(cls, instance: DirectorModel):
        return cls(
            id=instance.id,
            name=instance.name,
        )
