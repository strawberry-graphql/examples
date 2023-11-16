import strawberry


@strawberry.type
class Movie:
    imdb_id: str = strawberry.field(description="This is the IMDB ID of the movie")
    title: str
    year: int
    image_url: str
    imdb_rating: float
    imdb_rating_count: str
