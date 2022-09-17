.PHONY: all help update up up-d down ps frontend-shell backend-update backend-shell migrate makemigrations showmigrations db-shell django-shell mysql

all:
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

help:
	@egrep "^# target:" [Mm]akefile

## common
build:
	docker-compose -f docker-compose.development.yml build

debug-build:
	docker-compose -f docker-compose.development.yml build --no-cache --progress=plain

up:
	docker-compose -f docker-compose.development.yml up

up-d:
	docker-compose -f docker-compose.development.yml up -d

down:
	docker-compose -f docker-compose.development.yml down

ps:
	docker-compose -f docker-compose.development.yml ps

## frontend

frontend-shell:
	docker-compose -f docker-compose.development.yml exec frontend bash

## backend
backend-update:
	docker-compose -f docker-compose.development.yml run --rm backend pipenv install --system

backend-shell:
	docker-compose -f docker-compose.development.yml exec backend bash

migrate:
	docker-compose -f docker-compose.development.yml exec backend python3 manage.py migrate

makemigrations:
	docker-compose -f docker-compose.development.yml exec backend python3 manage.py makemigrations assignroom

showmigrations:
	docker-compose -f docker-compose.development.yml exec backend python3 manage.py showmigrations

db-shell:
	docker-compose -f docker-compose.development.yml exec db bash

django-shell:
	docker-compose -f docker-compose.development.yml exec backend python3 manage.py shell

mysql:
	docker-compose -f docker-compose.development.yml exec db mysql -urakuten -prakuten rakuten-db

dummy-data:
	docker-compose -f docker-compose.development.yml exec backend python3 manage.py loaddata dummy.json