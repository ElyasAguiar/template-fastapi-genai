"""Defines a custom exception for detailed error handling."""

from typing import Any


class CustomException(Exception):
    """Custom exception with detailed attributes."""

    def __init__(
        self,
        payload: Any = None,
        message: str = "",
        status_code: int = 422,
        error_log: str = "",
    ):
        super().__init__(message)
        self.payload = payload
        self.message = message
        self.status_code = status_code
        self.error_log = error_log

    def __str__(self) -> str:
        return (
            f"CustomException: {self.message} (Status Code: {self.status_code}, "
            f"Payload: {self.payload}, Error Log: {self.error_log})"
        )

    def to_dict(self) -> dict:
        """Return a dictionary representation of the exception."""
        return {
            "message": self.message,
            "payload": self.payload,
            "status_code": self.status_code,
            "error_log": self.error_log,
        }
