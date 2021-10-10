# Reddit GraphQL API

This example shows you how to create a Reddit API clone using GraphQL.
The goal of this example is not to re-create the entire reddit API, but
to produce a simpler version that is easier to understand, and implements
most of the features that Strawberry gives us.

## Tech Stack used:

- [Strawberry GraphQL](https://github.com/strawberry-graphql/strawberry)
- [FastAPI](https://github.com/tiangolo/fastapi) w/ [Starlette](https://github.com/encode/starlette)
- [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) (asyncio)
- [Alembic](https://github.com/sqlalchemy/alembic) for migrations

## Features at a glance

- [ ] Error handling with unions
- [ ] Authorization with the permissions API
- [ ] Batch loading with dataloaders
- [ ] Pagination with SQLAlchemy
- [x] modular codebase

## How to use

1. Install dependencies

Use [poetry](https://python-poetry.org/) to install dependencies:

```bash
poetry install
```

2. Setup database
   This example needs a PostgreSQL database. Make sure you have one on your machine.

3. Configure envionment variables
   Next up, you'd need to setup your environment variables. There is an example [`.env`](.env.example) file
   which you can reference! (Blank variables are optional)

4. Run migrations

Run [alembic](https://alembic.sqlalchemy.org/en/latest/) to create the database
and populate it with movie data:

```bash
poetry run alembic upgrade head
```

5. Run the server

Run [uvicorn](https://www.uvicorn.org/) to run the server:

```bash
poetry run uvicorn reddit:app --reload
```

You can now explore the GraphQL API here: http://localhost:8000/graphql
