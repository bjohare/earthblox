# Earth Blox Drone Supplier Registration

A full-stack demonstration application consisting of a `Vue.js` SPA frontend, a `django` middleware and a `postgres/postgis` database. The application also provides a [MailHog](https://github.com/mailhog/MailHog) docker instance for email testing as well as a [pgbouncer](https://www.pgbouncer.org/) instance for postgres connecion pooling and a [Redis](https://redis.io/) instance for http caching.

## Development

Install [Docker](https://docs.docker.com/install/) and [Docker-Compose](https://docs.docker.com/compose/).

To checkout the code run `git clone git@github.com:bjohare/earthblox.git`

To build and run a local instance of the stack do (from the local repo root):

`docker-compose -f local.yml up --build`

It will take a while to pull the docker containers and build the frontend. Once built the application will available at http://localhost:8000.

## Users

Two users are created by default. A admin (superuser) with login `admin@admin.com` password `admin`, and a demo user with a login of `demo@demo.com` password `demo`.
