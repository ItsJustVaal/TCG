# Load .env vars for local CLI use
include .env
export

DB_CONTAINER=TCGINFO
SCHEMA_FILE=db/schema.sql

# -------------------------------
# Infrastructure (Docker)
# -------------------------------

db-up: # Run the Postgres database and Adminer UI
	docker compose up -d

db-down: # Stop the database containers
	docker compose down

# -------------------------------
# Migrations (Alembic)
# -------------------------------

migration-new: # Create a new Alembic migration
	@read -p "Enter migration name: " name ; \
	alembic revision --autogenerate -m "$$name"

migrate-up: # Apply all migrations (upgrade to head)
	alembic upgrade head

migrate-down: # Roll back one migration (use with caution)
	alembic downgrade -1

migrate-reset: # Reset DB to base then re-apply all migrations (dev only)
	alembic downgrade base && alembic upgrade head

# -------------------------------
# Schema (for reference / tooling)
# -------------------------------

schema-dump: # Dump the live schema to schema.sql
	pg_dump --schema-only --no-owner --no-privileges -U $(POSTGRES_USER) -h $(POSTGRES_HOST) -d $(POSTGRES_DB) > $(SCHEMA_FILE)

# -------------------------------
# API Dev Utilities (FastAPI)
# -------------------------------

api-run: # Run FastAPI dev server with reload
	uvicorn app.main:app --reload

lint: # Lint (ruff)
	ruff check .

format: # Format (black)
	black .

test: # Run tests (pytest)
	pytest -q

# Default target
.DEFAULT_GOAL := help

# Print available commands
help:
	@echo "Available commands:"
	@awk 'BEGIN {FS = ":.*?#"} /^[a-zA-Z0-9_-]+:.*?#/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)
