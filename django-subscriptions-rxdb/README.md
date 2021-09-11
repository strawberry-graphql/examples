# django-subscriptions-rxdb

## tl;dr

This example reproduces the server-side component of the RxDB GraphQL example, with a couple of extras, which can be found [here](https://github.com/pubkey/rxdb/tree/master/examples/graphql). Checkout RxDB and run the GraphQL example. When running Ok, change `export const GRAPHQL_PORT = 10102;` and `export const GRAPHQL_SUBSCRIPTION_PORT = 10103;` ([lines 1 and 3 of this file](https://github.com/pubkey/rxdb/blob/master/examples/graphql/shared.js)) to equal `8000`. Then in the directory of this README file, `make install && make run`. More information about RxDB and GraphQL synchronisation can be found [here](https://rxdb.info/replication-graphql.html).

## Requirements

- [Clone of RxDB](https://github.com/pubkey/rxdb)
- [Python 3.8+](https://www.python.org/downloads/) (might work with other versions, not tested)
- [Poetry](https://python-poetry.org/)
- `make`
- [PostgreSQL](https://www.postgresql.org/) (optional)

Tested on Ubuntu 20.04, should work everywhere these are available with no changes.

## Reason for this example

While connectivity is getting better around the world every year, every user will always have moments when their connection is spotty (eg. on a plane). With an offline-first, local database and other offline-first tech (service workers, etc.), it is possible to develop web-technology-based applications that will continue to offer much of their functionality offline, with realtime sync when they are online. This really is the best of both worlds, and can give much more fluid and friendly usage when connections are spotty.

So you already have a Django-based app, and want to add some rich, client-side, offline-first functionality without starting from scratch? This is an example of some of the server-side code for one way of starting out.

The RxDB component of this is not included here to keep things as light as possible. Offline-first has complexities that need to be mastered, so this is not intended to be a template or even a particularly good way of doing things. It's one rough example to get you started with `rxdb`, `strawberry`, `django` and `broadcaster`.

### The full example stack

The example shows how you can do offline-realtime synchronisation of a local, RxDB database with Django. It uses Strawberry GraphQL subscriptions over websockets for the realtime sync capabilities. The default Django database configured in the `settings` file is Sqlite3 but there is also commented-out config for PostgreSQL.

If you use PostgreSQL then you will have to set up a database like you would for any PostgreSQL-powered Django site but if you do, the example will also then use PostgreSQL for the realtime notification functionality. To run the example with `postgres`, comment out the `sqlite3` config and put your `postgres` config in the settings file (src/demo/settings.py). You will also need to install extra deps with:

```
make install-postgres
```

Now run `make run` as usual to run it.

This extended setup shows how you can have multiple instances of your Django (in a Kubernetes cluster, for example), and realtime notifications will work for any client connected to any of the servers. This example uses [broadcaster](https://github.com/encode/broadcaster) for subscription notifications which, in addition to `postgres`, supports `memory` (for a single node), `redis` and `kafka`. If your `django` is not using `postgres` and/or you are using one of the other options for caching or messaging, you might want to use one of those. It should work if you follow the `broadcaster` docs for the connection string.
