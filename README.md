How to use:

If you want better vscode experience, create a virtual environment and install django

```
python -m venv .venv && source .venv/bin/activate
pip install django
```

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


 TODO: 
 
 1. Create 'Weather' App
 2. Setup Celery and Beat
 3. Setup 'Weather' data polling using Redis Streams
