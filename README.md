Local Development

> If you want better vscode experience, create a virtual environment and install django (`python -m venv .venv && source .venv/bin/activate` and `pip install django`)

## Start Project
Launch the containers using `make dev` <br />
Browse the web app - http://0.0.0.0:8000/

Migrations and Superuser commands:

```
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

Exec into Postgres `docker-compose exec db psql --username=postgres --dbname=donkey` and run SQL:

 - List databases: `\l`
 - Connect to databse: `\c donkey`
 - List tables: `\dt`
 - Select statement: `select * from auth_user;` (remember the ';')
 - Quit: `\q`


# Development Steps

High level steps required to create this solution.

## Install Django in Docker

1. Install Django app
```
pip install django
django-admin startproject hello_django .
python manage.py migrate
python manage.py runserver
```

2. Create Dockerfile and copy Django project in.
3. Create Docker-compose to build Docker and run Django Server.
4. Create Postgres service in Docker-compose.

## Create Weather App

1. Run Django manage.py
```
docker-compose exec web python manage.py startapp weather
```



 TODO: 

 1. Setup Celery and Beat
 2. Setup 'Weather' data polling using Redis Streams