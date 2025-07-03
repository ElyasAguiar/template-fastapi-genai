"""Monitor endpoints"""

from fastapi import APIRouter

from .health import health_router
from .metrics import metrics_router
from .root import root_router

monitor_router = APIRouter()

# Include routers for health endpoints and root endpoint
monitor_router.include_router(health_router, tags=["Default"])
monitor_router.include_router(root_router, tags=["Default"])
monitor_router.include_router(metrics_router, tags=["Default"])

__all__ = ["monitor_router"]
