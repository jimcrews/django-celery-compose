Local Development

> If you want better vscode experience, create a virtual environment and install django (`python -m venv .venv && source .venv/bin/activate` and `pip install django`)

## Start Project
Launch the containers using `make dev` <br />
Make migrations:

```
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

Browse the web app - http://0.0.0.0:8000/

---

Other potentially useful commands:

```
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py shell
```

Add Redis key:

```
docker-compose exec redis redis-cli

XADD weather:sydney * date 20240101 temperature 34 summary "Warm and Dry" fire_danger "MODERATE"
XADD weather:sydney * date 20240102 temperature 38 summary "Hot and Dry" fire_danger "EXTREME"
XADD weather:sydney * date 20240103 temperature 41 summary "Boiling Hot and Dry" fire_danger "CATASTROPHIC"
XADD weather:sydney * date 20240104 temperature 31 summary "Raining" fire_danger "LOW"
```

Celery docker logs should show the new message
```
Hey this works
Task weather.tasks.redis_weather_listener succeeded
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

# Add Celery and Beat

1. Add celery and redis to requirements.txt
2. Set the Weather app as a celery app by configuring __init__.py and creating the celery.py and task.
3. Add celery settings
4. Config docker-compose
5. Test by adding a key into redis

