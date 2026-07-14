# Project Name

This repository contains the initial skeleton for a full‑stack application using:

- FastAPI (backend)
- Next.js (frontend)

This commit includes only the project structure and tooling. Application features will be added in future commits.

## Running the Backend

From the project root:

```bash
cd backend
make dev
```
The backend runs on http://localhost:8000

## ORM

The backend uses SQLAlchemy declarative ORM with sessionmaker and Alembic for migration support.

## Environment

The app reads DATABASE_URL from environment variables (or .env when present). The current default is a local SQLite database: sqlite:///./app.db.

## Migrations

Migration tooling is available via Alembic:

```bash
cd backend
make migrate
```

At this time, schema/migrations are not yet defined, so this is the migration workflow for future database changes.

## Running the Frontend

From the project root:

```bash
frontend/run.sh
```
The frontend runs on http://localhost:3000

## Tech Stack

### Backend
- FastAPI
- Uvicorn
- Python 3.11
- Black + isort (formatting)

### Frontend
- Next.js
- Node.js
- Prettier (formatting)

### Repo
- Git
- README
- Dev run scripts
