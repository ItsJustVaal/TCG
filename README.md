# TCG Meta Tracker

A web application that aggregates and displays deck data for **One Piece TCG** and **Hololive TCG** (to start, more can be added later), showing popular cards by set, archetype, and tournament usage.  
The goal is to provide statistics on the most commonly used cards across all sets based on recent tournament data.  
This will allow users to know which cards to keep or stock up on based on current and future information.

## Features

- PostgreSQL database for storing sets, cards, decks, etc.
- REST API for querying cards and decks by usage, archetype etc.

## Current Technologies Used

Go, Chi, PostgreSQL, sqlc, Goose

---

## Project Structure

```bash
├── api/                 # Route handlers
├── cmd/api/             # Main server entry point
├── configs/             # Config/env loading
├── frontend/            # (Optional) React app
├── internal/            # App logic (db, cache, etc.)
├── internal/migrations  # Goose migrations
├── internal/queries     # SQLC queries
├── internal/schema      # SQLC schema dump
├── scripts/             # Utility scripts
├── models/              # Structs
├── test/                # Go tests
├── docker-compose.yml
├── .env
```

## Work In Progress

- This is just the init of the project, nothing has been built out but much has been planned
- Unsure what frontend framework I will use so I just put React in the comments for now
