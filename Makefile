
dev:
	docker-compose build
	docker-compose up -d

clean:
	docker-compose down
	docker-compose down --volumes 
	docker-compose down --rmi local

migrate:
	docker-compose exec web python manage.py makemigrations
	docker-compose exec web python manage.py migrate
