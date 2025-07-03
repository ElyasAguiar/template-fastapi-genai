"""Root router"""

from fastapi import APIRouter

from app import settings
from app.core.responses import AppJSONResponse

health_router = APIRouter()


@health_router.get(
    "/health",
    response_class=AppJSONResponse,
    summary="Root",
    description="Endpoint of service (/)",
    response_description="JSON response indicating the root message of the service.",
)
async def root():
    """Endpoint for root."""
    return AppJSONResponse(
        data={"message": "FastAPI Boilerplate", "version": settings.RELEASE_VERSION},
        message="Service root endpoint",
        status="success",
        status_code=200,
    )
