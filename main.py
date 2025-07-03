"""Entry point to run the application"""

import multiprocessing
import subprocess
import sys

import uvicorn
from loguru import logger

from app.core.config import AppEnvs, settings


def calculate_worker_count() -> int:
    """Calculate optimal worker count: 2 * CPU cores + 1"""
    return multiprocessing.cpu_count() * 2 + 1


def main():
    """Start the FastAPI application with uvicorn (for development only)."""
    worker_count = settings.WORKER_COUNT or calculate_worker_count()
    logger.info(f"🚀 Starting application with {worker_count} worker(s)")
    uvicorn.run(
        app="app.core.server:app",
        host=settings.HOST,
        port=settings.PORT,
        workers=worker_count,
        reload=settings.ENVIRONMENT == "development",
    )


if __name__ == "__main__":
    if settings.ENVIRONMENT == AppEnvs.PRODUCTION:
        logger.info("✅ Production environment detected. Launching with Gunicorn...")
        try:
            subprocess.run(["./start.sh"], check=True)
        except subprocess.CalledProcessError as e:
            logger.error(f"❌ Failed to start production server: {e}")
        sys.exit(0)

    main()
