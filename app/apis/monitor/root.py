"""Root router"""

from fastapi import APIRouter
from fastapi.responses import RedirectResponse

root_router = APIRouter()


@root_router.get(
    "/",
    include_in_schema=False,
    summary="Root Redirect",
    description="Redirects the root path to the interactive API documentation (/docs).",
    response_description="Redirect response to /docs",
)
async def root():
    """Redirects to the API documentation."""
    return RedirectResponse(url="/docs")
