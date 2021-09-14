from asgiref.sync import sync_to_async
from typing import List, Optional
import strawberry

from movies.models import Director as DirectorModel


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


@sync_to_async
def load_directors(keys) -> List[Optional[Director]]:
    qs = DirectorModel.objects.filter(id__in=keys)
    directors_map = {director.id: director for director in qs}

    directors = []
    for key in keys:
        maybe_director = directors_map.get(key)
        if maybe_director:
            directors.append(Director.from_instance(maybe_director))
        else:
            directors.append(None)
    return directors
