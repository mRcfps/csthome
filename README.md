# CSTHome

Server-side codebase of DongHua University party building project.

## Get Up and Running Locally

### Using Virtual Environment

Make sure you have the following on your host:

- python3
- virtualenv
- pip
- PostgreSQL

First things first.

1. [Create a virtualenv](https://virtualenv.pypa.io/en/stable/userguide/).

2. Activate the virtualenv you have just created (Here my virtualenv is named `venv`).

```bash
$ source venv/bin/activate
```

3. Install development requirements:

```bash
(venv)$ pip install -r requirements/local.txt
```

4. Configure PostgreSQL:

```
$ psql
psql=# CREATE USER csthome WITH PASSWORD 'csthome';
psql=# CREATE DATABASE csthome OWNER csthome;
psql=# ALTER USER csthome CREATEDB;
psql=# GRANT ALL PRIVILEGES ON DATABASE csthome to csthome;
```

5. Apply migrations:

```bash
$ python manage.py migrate
```

6. See the application being served through Django development server:

```bash
$ python manage.py runserver
```

### Using Docker

Install [Docker](https://docs.docker.com/install/#supported-platforms) and [Docker Compose](https://docs.docker.com/compose/install/), and run the following command:

```bash
$ docker-compose -f local.yml up --build
```

Or you can emulate **production** environment with `production.yml`:

```bash
$ docker-compose -f production.yml up --build
```

Whenever a switch is needed, just do it!

## Deployment

In this project we use **fabric** for automated deployment. Please note that **fabric** is only supported on Python 2 platform.

```bash
$ pip install fabric
$ fab deploy
```

You have to put RSA certificate within the project directory. Please contact mrc to get it.
