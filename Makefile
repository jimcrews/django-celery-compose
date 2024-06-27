
dev:
	$(info ************  Spinning up Docker ************)
	docker-compose build
	docker-compose up -d
