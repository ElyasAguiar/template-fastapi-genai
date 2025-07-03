"""Logging middleware with request ID tracing and default function ID handling."""

import contextvars
import uuid

from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from app.core.config import AppEnvs, settings

# Context variable to store request ID per request
request_id_ctx_var = contextvars.ContextVar("request_id", default=None)

# Determine the environment (e.g., development, production)
APP_ENV = settings.ENVIRONMENT.lower()


def add_request_id_to_log(record: dict) -> None:
    """Inject request ID and default function ID into log records."""
    record["extra"]["request_id"] = request_id_ctx_var.get() or "N/A"
    record["extra"].setdefault("function_id", "N/A")


# Configure logger with context patcher
logger.configure(patcher=add_request_id_to_log)  # type: ignore

# Define log format
LOG_FORMAT = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level:<8}</level> | "
    "RequestID=<cyan>{extra[request_id]}</cyan> | "
    "FuncID=<magenta>{extra[function_id]}</magenta> | "
    "<level>{message}</level>\n"
)

# Remove default logger and add our custom configuration
logger.remove()
logger.add(
    sink=lambda msg: print(msg, end=""),
    format=LOG_FORMAT,
    level=settings.LOG_LEVEL.upper(),
    enqueue=True,
    colorize=True,
)


class LoggingMiddleware(BaseHTTPMiddleware):
    """Middleware to log incoming HTTP requests and responses."""

    async def dispatch(self, request: Request, call_next) -> Response:
        # Skip logging for /metrics endpoint
        if (
            request.url.path == "/metrics"
            or request.url.path == "/docs"
            or request.url.path == "/health"
            or request.url.path == "/openapi.json"
            or request.url.path == "/"
        ):
            return await call_next(request)

        # Set or generate request ID
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        request_id_ctx_var.set(request_id)  # type: ignore
        request.state.request_id = request_id

        try:
            # Log request body in non-production
            if APP_ENV in {AppEnvs.DEVELOPMENT, AppEnvs.QA, AppEnvs.DEMO}:
                body_bytes = await request.body()
                body_text = body_bytes.decode("utf-8", errors="ignore").strip()
                logger.debug(
                    f"📥 Request: {request.method} {request.url.path} | Body: {body_text or 'empty'}"
                )

            # Process the request
            response = await call_next(request)

        except Exception as e:
            logger.exception(
                f"❌ Error while processing {request.method} {request.url.path}: {str(e)}"
            )
            raise

        # Attach request ID to response
        response.headers["X-Request-ID"] = request_id
        return response
