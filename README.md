# API Yamdb Project

![Deploy](https://github.com/alidzen/yamdb_final/workflows/Yamdb%20workflow/badge.svg)

API for working with titles, genres, reviews based on Django Framework

## Prerequisites

Docker should be installed and running on your local machine. For more information
see [Docker Get Started Documentation](https://www.docker.com/get-started)

## Installation

Clone repository from GitHub

```sh
$ git clone https://github.com/alidzen/yamdb_final.git
$ cd yamdb_final
```

## Run project

### Run docker

```sh
$ docker-compose up
```

### Migrate db

```sh
$ docker exec -it CONTAINER_ID python manage.py migrate
```

### Load fixtures data for db

```sh
$ docker exec -it CONTAINER_ID python manage.py loaddata fixtures.json 
```

### Create superuser

```sh
$ docker exec -it CONTAINER_ID python manage.py createsuperuser
```

### Collect static

```sh
$ docker exec -it CONTAINER_ID python manage.py collectstatic
```

Done! The project will be running at http://0.0.0.0:8000/

## Useful urls:

- http://0.0.0.0:8000/api/v1/titles/ — See created Titles without any permissions
- http://0.0.0.0:8000/redoc — Detailed information about how API works

**After deployment the project will be available on http://178.154.234.255/** 

## About author

Denis Golubtsov is a student of the 7th backend faculty of Y.Praktikum

## Used technologies

- Python
- Django
- Postgres
- Docker
