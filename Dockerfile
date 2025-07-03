FROM python:3.12-slim-bullseye

ENV PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1

WORKDIR /app

# Install system dependencies and uv
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl gcc libc-dev python3-dev \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install --upgrade pip uv

# Copy dependency files and install dependencies
COPY pyproject.toml uv.lock* /app/
RUN uv pip install --system pyproject.toml

# Copy application code
COPY . /app

# Expose app port
EXPOSE 8004

# Default run command
CMD ["uv", "run", "python", "main.py"]
