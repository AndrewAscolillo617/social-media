# Use the project root virtual environment
VENV = ../.venv/bin

# Run FastAPI backend
dev:
	$(VENV)/uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Run Alembic migrations
migrate:
	$(VENV)/alembic upgrade head

# Create a new Alembic revision
revision:
	$(VENV)/alembic revision --autogenerate -m "$(msg)"

# Format code (Black + isort)
fmt:
	$(VENV)/black .
	$(VENV)/isort .
