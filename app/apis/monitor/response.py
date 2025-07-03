"""Response module for health check"""

from fastapi.responses import JSONResponse


class HealthCheckResponse(JSONResponse):
    """Custom response class for health checks."""

    def __init__(self, content: dict, status_code: int = 200):
        """
        Initialize the HealthCheckResponse.

        Args:
            content (dict, optional): A dictionary containing the health check status.
            status_code (int, optional): HTTP status code.
        """
        super().__init__(content=content, status_code=status_code)


class RootResponse(JSONResponse):
    """Custom response class for root."""

    def __init__(self, content: dict, status_code: int = 200):
        """
        Initialize the RootResponse.

        Args:
            content (dict, optional): A dictionary containing the root payload.
            status_code (int, optional): HTTP status code.
        """
        super().__init__(content=content, status_code=status_code)
