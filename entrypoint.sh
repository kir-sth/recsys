#!/bin/sh

export PYTHONPATH=/app

# Wait for the database to be ready
while ! nc -z ${POSTGRES_HOST} ${POSTGRES_PORT}; do
  echo "Waiting for database..."
  sleep 1
done

alembic revision --autogenerate -m "init"
alembic upgrade head

# Start the application
exec uvicorn app.main:app --host $FASTAPI_HOST --port $FASTAPI_PORT