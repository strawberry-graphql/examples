# Example of a GraphQL API using Strawberry and FastAPI

This examples shows you how to setup Strawberry with FastAPI

## How to use

1. Install dependencies

Use [poetry](https://python-poetry.org/) to install dependencies:

```bash
poetry install
```

2. Run the server

Run [uvicorn](https://www.uvicorn.org/) to run the server:

```bash
poetry run uvicorn main:app --reload
```

3. Access the GraphiQL IDE and explore the schema at [http://localhost:8000/graphql](http://localhost:8000/graphql)

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
