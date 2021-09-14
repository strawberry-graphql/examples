from asgiref.sync import sync_to_async
import strawberry

from movies.models import Movie as MovieModel

from .director import Director


@sync_to_async
def get_director(movie):
    return movie.director


@strawberry.type
class Movie:
    id: int
    imdb_id: str
    title: str
    year: int
    image_url: str
    imdb_rating: float
    imdb_rating_count: str

    instance: strawberry.Private[MovieModel]

    @strawberry.field
    async def director(self, info) -> Director:
        loader = info.context["dataloaders"]["director_loader"]
        director = await loader.load(self.instance.director_id)
        return Director.from_instance(director)

    @classmethod
    def from_instance(cls, instance: MovieModel):
        return cls(
            instance=instance,
            id=instance.id,
            imdb_id=instance.imdb_id,
            title=instance.title,
            year=instance.year,
            image_url=instance.image_url,
            imdb_rating=instance.imdb_rating,
            imdb_rating_count=instance.imdb_rating_count,
        )
