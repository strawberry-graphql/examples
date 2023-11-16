from typing import List

import json
import strawberry

from .definitions.movie import Movie


@strawberry.type
class Query:
    @strawberry.field
    def top_rated_movies(self, info, limit: int = 250) -> List[Movie]:
        with open("../common-data/movies.json", "r") as file:
            data = json.load(file)

        result = []

        for i in range(limit):
            result.append(
                Movie(
                    imdb_id=data[i]["imdb_id"],
                    title=data[i]["title"],
                    year=data[i]["year"],
                    image_url=data[i]["image_url"],
                    imdb_rating=data[i]["imdb_rating"],
                    imdb_rating_count=data[i]["imdb_rating_count"],
                )
            )

        return result


schema = strawberry.Schema(Query)
