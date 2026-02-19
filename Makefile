.PHONY: dev test lint ingest up down

dev:
	docker compose up --build

test:
	docker compose run --rm api pytest -q

lint:
	docker compose run --rm api ruff check app tests && docker compose run --rm api mypy app

ingest:
	docker compose run --rm api python scripts/ingest.py

up:
	docker compose up -d --build

down:
	docker compose down -v
