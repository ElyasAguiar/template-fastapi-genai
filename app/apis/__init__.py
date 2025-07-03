"""API Router Configuration"""

from fastapi import APIRouter

from .monitor import monitor_router
from .v1 import v1_routers

# Initialize the main application router
api_routers = APIRouter()
api_routers.include_router(monitor_router)
api_routers.include_router(v1_routers, prefix="/api/v1")

__all__ = ["api_routers"]
