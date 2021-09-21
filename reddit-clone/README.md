# Reddit GraphQL API

This example shows you how to create a Reddit API clone using GraphQL.

## Tech Stack used:

- Strawberry GraphQL
- FastAPI w/ Starlette
- SQLAlchemy (asyncio)
- Alembic for migrations

## Features at a glance

- Error handling with unions
- Authorization with the permissions API
- Batch loading with dataloaders
- Pagination with SQLAlchemy

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
poetry run uvicorn reddit:app --reload
```

The GraphQL API should now be available at http://localhost:8000/graphql
