"""User service"""

from typing import Any, Tuple

from app import trace

from .models import CreateUserRequest


class UserService:
    """User service."""

    def __init__(self) -> None:
        """Initialize the service."""
        pass

    @trace(name="sample_function")
    async def sample_function(self, temp_arg: str) -> str:
        """Convert input string to uppercase."""
        return temp_arg.upper()

    @trace(name="create_user_service")
    async def create_user_service(
        self, request_params: CreateUserRequest
    ) -> Tuple[Any, str, int]:
        """Create a new user from request parameters."""
        await self.sample_function(temp_arg=request_params.name)

        payload = {
            "user_id": 1,
            "name": request_params.name,
            "email": request_params.email,
        }
        message = "User created successfully"
        status_code = 201
        return payload, message, status_code
