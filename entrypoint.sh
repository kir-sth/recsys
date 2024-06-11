#!/bin/sh

export PYTHONPATH=/WORKDIR

sleep 5
alembic revision --autogenerate -m "init"
alembic upgrade head

# Start the application
python3 app/main.py
