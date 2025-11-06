# TCG Meta Tracker

A web application that aggregates and displays deck data for **One Piece TCG** and **Hololive TCG** (to start, more can be added later), showing popular cards by set, archetype, and tournament usage.  
The goal is to provide statistics on the most commonly used cards across all sets based on recent tournament data.  
This will allow users to know which cards to keep or stock up on based on current and future information.

## Features

- PostgreSQL database for storing sets, cards, decks, etc.
- FastAPI REST API for querying cards, sets, and decks by usage, archetype, and more.
- Async SQLAlchemy 2.0 + asyncpg for database access.
- Redis for caching common queries (e.g., popular cards per set).
- Alembic for schema migrations.
- uvicorn for ASGI serving and concurrency.

## Current Technologies Used

Python (FastAPI, SQLAlchemy, Alembic, asyncpg, Redis), PostgreSQL, Docker Compose

## Project Structure

```bash
├── app/
│   ├── api/                 # Routers (v1), deps, middleware
│   │   ├── v1/
│   │   └── middleware/
│   ├── core/                # settings/config, logging, startup events
│   ├── db/                  # session, base, repositories
│   │   ├── models/          # SQLAlchemy models
│   │   └── seed/            # optional seed data
│   ├── schemas/             # Pydantic models (request/response)
│   ├── services/            # business logic, caching, search, etc.
│   │   └── ingest/          # your “scraper” & card importers live here
│   ├── migrations/          # Alembic
│   ├── main.py              # FastAPI app instance
│   └── __init__.py
│
├── frontend/                # React (or other)
├── scripts/                 # admin/ops scripts (invoke/Make targets call these)
├── tests/
│   ├── unit/
│   └── integration/
│
```

## Work In Progress

- This is just the init of the project, nothing has been built out but much has been planned
- Unsure what frontend framework I will use so I just put React in the comments for now
