"""Expose Prometheus metrics endpoint for monitoring."""

from fastapi import APIRouter, Response
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest

metrics_router = APIRouter()


@metrics_router.get("/metrics", include_in_schema=True)
async def metrics():
    """Return Prometheus-formatted metrics response."""
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
