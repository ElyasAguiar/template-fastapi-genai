"""Response module for application-level API responses."""

from typing import Any, Literal, Optional, Union

from fastapi.responses import JSONResponse


class AppJSONResponse(JSONResponse):
    """Custom JSON response structure for the entire application.

    This class standardizes all API responses to follow a consistent structure,
    making it easier for frontend clients and developers to interpret results.
    """

    def __init__(
        self,
        data: Any = None,
        message: str = "Success",
        status: Literal["success", "error"] = "success",
        error: Optional[Union[str, dict]] = None,
        status_code: int = 200,
    ):
        """Initializes the AppJSONResponse.

        Args:
            data (Any, optional): The actual payload to return in the 'data' key. Defaults to None.
            message (str, optional): A human-readable message describing the result. Defaults to "Success".
            status (Literal, optional): Status of the response; typically 'success' or 'error'. Defaults to "success".
            error (Union[str, dict], optional): Optional error details, either a string or a dictionary. Defaults to None.
            status_code (int, optional): HTTP status code for the response. Defaults to 200.
        """
        content = {
            "status": status,
            "message": message,
            "data": data,
            "error": error,
        }
        super().__init__(
            content=content,
            status_code=status_code,
            media_type="application/json",
        )
