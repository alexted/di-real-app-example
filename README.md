# di-real-app-example

fdevadfve r r rr rrweeqrrcvr b ertwevrqwd

## Authors

Alex Ted

## Implementation language

Python 3.13

## Deployment environment

Kubernetes

## Documentation

TODO

## Interaction with 3rd party services

TODO

## Scalability

Scalability is done by `Kubernetes` tools, by adding additional pods.
It is possible to scale by `granian`, by adding additional workers.

## Dependencies

pre-requisites:

```bash
$ poetry new di-real-app-example && cd $_        // create a project virtual environment
```

Install the necessary packages:

```bash
(di-real-app-example)$ poetry install                // install all project dependencies
(di-real-app-example)$ poetry install --only main    // install only main project dependencies
```

**Important**:
before running in a container, be sure to execute the ``poetry install'' command,
command to generate poetry.lock - this is the file from which information about dependencies is to be taken when
building the image.
You must also add this file to the git index.

## Startup inside Docker

```bash
$ docker compose up
```

## Set pre-commit hook

```bash
$ pre-commit install
```

## Linter

```bash
$ python -m ruff format && python -m ruff check --fix --unsafe-fixes
```

## Run tests

```bash
$ python -m pytest -vvs
```

## Environment variables

These are the environment variables that you can set for the app to configure it and their default values:

#### `ENVIRONMENT`

String value which defines the runtime environment in which the application runs.

Can have the following values:

* `LOCAL`  *default*
* `TEST`
* `STAGE`
* `PROD`

#### `APP_NAME`

The string variable defining the service name.

By default: `di-real-app-example`

### Logging

#### `LOG_LEVEL`

String value which defines the logging severity.

Can have the following values:

* `CRITICAL`
* `ERROR`
* `WARNING`
* `INFO`  *default*
* `DEBUG`

#### `SENTRY_URL`

The url that defines address of the Sentry service.

By default, it's not set.

### IdP

#### `IDP_URL`

The url of the Identity and Access Management (IDP) service.

By default, it's not set.

#### `IDP_PUBLIC_KEY`

The public key of the Identity and Access Management (IdP) service.

By default, it's not set.

#### `IDP_CLIENT_SECRET`

The credentials secret of the client (service).

By default, it's not set.

### Databases, MessageBrokers

#### `POSTGRES_DSN`

The dsn that defines connection string to of the PostgreSQL.

By default, it's not set.

#### `POSTGRES_MAX_CONNECTIONS`

The int value to setting to limit the number of connections (and resources that are consumed by connections) to the
PostgreSQL.

By default, it's `10`.

#### `CACHE_DSN`

The dsn that defines connection string to of the cache server.

By default, it's not set.

#### `KAFKA_DSN`

The dsn that defines connection string to of the Kafka.

By default, it's not set.

