# Load .env vars for local CLI use
include .env
export

DB_CONTAINER=TCGINFO
SCHEMA_FILE=db/schema.sql


db-up: # Run the Postgres database and Adminer UI
	docker compose up -d


db-down: # Stop the database containers
	docker compose down


migration-new: # Create a new migration
	@read -p "Enter migration name: " name ; \
	goose -dir internal/db/migrations create $$name sql


migrate-up: # Apply all migrations
	goose -dir internal/db/migrations postgres "$(DB_URL)" up


migrate-down: # Roll back one migration (use with caution)
	goose -dir internal/db/migrations postgres "$(DB_URL)" down


migrate-reset: # Roll back all migrations (dev only)
	goose -dir internal/db/migrations postgres "$(DB_URL)" reset


schema-dump: # Dump the live schema to schema.sql (used by sqlc)
	pg_dump --schema-only --no-owner --no-privileges -U $(POSTGRES_USER) -h $(POSTGRES_HOST) -d $(POSTGRES_DB) > $(SCHEMA_FILE)


sqlc-generate: # Generate Go code from SQL files
	sqlc generate


gen: # Chain schema update + sqlc
	make schema-dump && make sqlc-generate

lint: # Run Go linter
	go fmt ./...

test: # Run Go tests
	go test ./...


build: # Build the Go binary
	go build -o bin/tcg cmd/api/main.go

# Default target
.DEFAULT_GOAL := help

# Print available commands
help:
	@echo "Available commands:"
	@awk 'BEGIN {FS = ":.*?#"} /^[a-zA-Z0-9_-]+:.*?#/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)
