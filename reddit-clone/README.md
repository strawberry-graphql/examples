# Reddit GraphQL API

This example shows you how to create a Reddit API clone using GraphQL.
The goal of this example is not to re-create the entire reddit API, but
to produce a simpler version that is easier to understand, and implements
most of the features that Strawberry gives us.

## Tech Stack used:

- [Strawberry GraphQL](https://github.com/strawberry-graphql/strawberry)
- [Starlette](https://github.com/encode/starlette) web framework
- [Uvicorn](https://github.com/encode/uvicorn) ASGI server
- [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy) core/ mapper (asyncio)
- [Alembic](https://github.com/sqlalchemy/alembic) migrations
- [PostgreSQL](https://github.com/postgres/postgres) database server
- [Schematics](https://github.com/schematics/schematics) data validation
- [Celery](https://github.com/celery/celery) tasks ([Redis](https://github.com/redis/redis) store, [RabbitMQ](https://github.com/rabbitmq/rabbitmq-server) broker)

## Features at a glance

- [ ] Implements the Relay spec
- [x] data modelling with relations
- [x] Error modelling within the schema
- [ ] Authorization with the permissions API
- [x] Batch loading with dataloaders
- [x] modular codebase

## How to use

You can use [Docker Compose](https://github.com/docker/compose) to run this example. Make sure you have it installed on your machine!

```text
docker compose up
```

You can now explore the GraphQL API here: http://localhost/graphql
