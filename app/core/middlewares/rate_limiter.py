"""Rate limiter configuration and utility exports using fastapi-limiter."""

import fakeredis.aioredis
import redis.asyncio as redis
from fastapi import Request
from fastapi_limiter import FastAPILimiter

from app.core.config import RateLimitBackend, settings


async def token_or_ip_key(request: Request) -> str:
    """Use Bearer token from Authorization header if available, otherwise fallback to client IP address."""
    auth_header = request.headers.get("authorization")
    if auth_header and auth_header.lower().startswith("bearer "):
        token = auth_header.removeprefix("Bearer ").strip()
        if token:
            return token
    # Fallback to IP
    return request.client.host


async def init_rate_limiter():
    """Initialize FastAPI rate limiter with local or Redis backend."""

    if settings.RATE_LIMIT_BACKEND == RateLimitBackend.LOCAL:
        fake_redis = fakeredis.aioredis.FakeRedis()
        await FastAPILimiter.init(redis=fake_redis, identifier=token_or_ip_key)

    elif settings.RATE_LIMIT_BACKEND == RateLimitBackend.REDIS:
        redis_url = f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}"
        if settings.REDIS_PASSWORD:
            redis_url = f"redis://:{settings.REDIS_PASSWORD}@{settings.REDIS_HOST}:{settings.REDIS_PORT}"

        redis_client = redis.from_url(redis_url, decode_responses=True)
        await FastAPILimiter.init(redis_client, identifier=token_or_ip_key)

    else:
        raise ValueError(
            f"Unsupported RATE_LIMIT_BACKEND: {settings.RATE_LIMIT_BACKEND}"
        )
