# FastAPI + SQLAlchemy

This examples shows you how to setup Strawberry with FastAPI and SQLAlchemy. It
setups a GraphQL API to fetch the top rated movies from IMDB (stored in a sqlite
DB).

## How to use

1. Install dependencies

Use [poetry](https://python-poetry.org/) to install dependencies:

```bash
poetry install
```

2. Run migrations

Run [alembic](https://alembic.sqlalchemy.org/en/latest/) to create the database
and populate it with movie data:

```bash
poetry run alembic upgrade head
```

3. Run the server

Run [uvicorn](https://www.uvicorn.org/) to run the server:

```bash
poetry run uvicorn main:app --reload
```

The GraphQL API should now be available at http://localhost:8000/graphql

## Example query

```graphql
query AllTopRatedMovies {
  topRatedMovies {
    id
    imageUrl
    imdbId
    imdbRating
    imdbRatingCount
    title
    year
    director {
      id
      name
    }
  }
}
```
