#!/bin/bash

# Load environment variables from .env
set -a
source .env
set +a

# Default values if not set in .env
HOST="${HOST:-0.0.0.0}"
PORT="${PORT:-8000}"
APP_MODULE="app.core.server:app"
WORKERS=$(python3 -c "import multiprocessing; print(multiprocessing.cpu_count() * 2 + 1)")

echo "🚀 Starting FastAPI app with Gunicorn on $HOST:$PORT with $WORKERS workers..."

exec gunicorn "$APP_MODULE" \
    --worker-class uvicorn.workers.UvicornWorker \
    --workers "$WORKERS" \
    --bind "$HOST:$PORT"
