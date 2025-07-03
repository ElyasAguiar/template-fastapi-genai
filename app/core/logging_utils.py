"""Decorator to trace and log function calls with timing, args, result, and a unique function ID."""

import asyncio
import functools
import json
import time
import uuid

from loguru import logger


def trace(name: str = "", log_args: bool = True, log_result: bool = True):
    """Trace and log function execution with a unique function ID."""

    def decorator(func):
        """Wrap function to add tracing and logging."""

        def format_args(args, kwargs):
            """Format function arguments for logging."""
            try:
                return json.dumps(
                    {"args": [str(a) for a in args], "kwargs": kwargs}, default=str
                )
            except Exception:
                return "[Unserializable]"

        def format_result(result):
            """Format function result for logging."""
            try:
                return json.dumps(result, default=str)
            except Exception:
                return "[Unserializable]"

        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            """Async wrapper to log execution details and handle exceptions."""
            function_id = str(uuid.uuid4())
            log = logger.bind(function_id=function_id)
            label = name or func.__qualname__

            log.trace(f"🔍 [{label}] START")
            if log_args:
                log.trace(f"📥 [{label}] ARGS: {format_args(args, kwargs)}")

            start = time.perf_counter()
            try:
                result = await func(*args, **kwargs)
                duration = time.perf_counter() - start

                if log_result:
                    log.trace(f"📤 [{label}] RESULT: {format_result(result)}")

                log.trace(f"✅ [{label}] END ({duration:.2f}s)")
                return result
            except Exception as e:
                log.exception(f"💥 [{label}] FAILED | Error: {e}")
                raise

        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            """Sync wrapper to log execution details and handle exceptions."""
            function_id = str(uuid.uuid4())
            log = logger.bind(function_id=function_id)
            label = name or func.__qualname__

            log.trace(f"🔍 [{label}] START")
            if log_args:
                log.trace(f"📥 [{label}] ARGS: {format_args(args, kwargs)}")

            start = time.perf_counter()
            try:
                result = func(*args, **kwargs)
                duration = time.perf_counter() - start

                if log_result:
                    log.trace(f"📤 [{label}] RESULT: {format_result(result)}")

                log.trace(f"✅ [{label}] END ({duration:.2f}s)")
                return result
            except Exception as e:
                log.exception(f"💥 [{label}] FAILED | Error: {e}")
                raise

        return async_wrapper if asyncio.iscoroutinefunction(func) else sync_wrapper

    return decorator
