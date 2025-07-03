# 🛡️ Rate Limiting with fastapi-limiter

This project uses [**fastapi-limiter**](https://github.com/long2ice/fastapi-limiter) to implement scalable, Redis-based rate limiting in your FastAPI app. It protects against abuse, brute force attempts, and excessive traffic by enforcing flexible request thresholds.

---

## 🚀 Features

- 🔗 Redis-backed distributed rate limiting
- 🧠 IP or token-based client identification
- 🪝 Decorator-free, dependency-based integration
- 🧾 Automatic `429 Too Many Requests` responses
- 🕒 Native `Retry-After` header support
- ⚙️ Customizable via `Bearer` tokens, IPs, headers, or API keys

---

## ⚙️ Configuration

### 🔧 Backend Initialization

Rate limiter is initialized in `app/core/middlewares/rate_limiter.py`:

```python
"""Rate limiter configuration using fastapi-limiter."""

import fakeredis.aioredis
import redis.asyncio as redis
from fastapi import Request
from fastapi_limiter import FastAPILimiter

from app.core.config import RateLimitBackend, settings


async def token_or_ip_key(request: Request) -> str:
    """Use Bearer token if available, fallback to client IP."""
    auth_header = request.headers.get("authorization")
    if auth_header and auth_header.lower().startswith("bearer "):
        token = auth_header.removeprefix("Bearer ").strip()
        if token:
            return token
    return request.client.host


async def init_rate_limiter():
    """Initialize FastAPI limiter with Redis or local memory (fakeredis)."""

    if settings.RATE_LIMIT_BACKEND == RateLimitBackend.LOCAL:
        fake_redis = fakeredis.aioredis.FakeRedis(decode_responses=True)
        await FastAPILimiter.init(redis=fake_redis, identifier=token_or_ip_key)

    elif settings.RATE_LIMIT_BACKEND == RateLimitBackend.REDIS:
        redis_url = f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}"
        if settings.REDIS_PASSWORD:
            redis_url = f"redis://:{settings.REDIS_PASSWORD}@{settings.REDIS_HOST}:{settings.REDIS_PORT}"

        redis_client = redis.from_url(redis_url, decode_responses=True)
        await FastAPILimiter.init(redis=redis_client, identifier=token_or_ip_key)

    else:
        raise ValueError(
            f"Unsupported RATE_LIMIT_BACKEND: {settings.RATE_LIMIT_BACKEND}"
        )
```

### ⚡ Lifespan Hook

Call it inside your app’s `lifespan` startup:

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI

from .middlewares.rate_limiter import init_rate_limiter

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_rate_limiter()
    yield
```

---

## 🧩 Usage in Routes

### ✅ Limit Requests per IP/Token

Use the `RateLimiter` dependency in route decorators:

```python
from fastapi import APIRouter, Depends
from fastapi_limiter.depends import RateLimiter

router = APIRouter()

@router.get("/ping", dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def ping():
    return {"message": "pong"}
```

This will limit requests to **10 per 60 seconds** per token or IP.

---

## 🧠 Custom Key Strategies

You can implement any logic in `token_or_ip_key`, for example:

```python
# Use X-API-KEY header
async def api_key_or_ip(request: Request) -> str:
    return request.headers.get("X-API-KEY") or request.client.host
```

---

## 🛑 Handling 429 Responses

A `429 Too Many Requests` response is returned automatically, but you can customize it inside your app’s exception handlers:

```python
def _handle_fastapi_http_exception(self):
        """Handle FastAPI HTTP exceptions."""

    @self.app.exception_handler(HTTPException)
    async def fastapi_http_exception_handler(request: Request, exc: HTTPException):
        if exc.status_code == 429:
            headers = getattr(exc, "headers", {})
            retry_after = int(headers["Retry-After"])

            return await self._create_json_response(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                message=messages.RATE_LIMIT_ERROR.format(retry_after=retry_after),
                error_log=str(exc),
            )

        return await self._create_json_response(
            status_code=exc.status_code, message=exc.detail
        )
```

---

## 🐳 Redis Setup for Local Dev

You can use Docker to run Redis locally:

```bash
docker run -d --name dev-redis -p 6379:6379 redis:7-alpine
```

### Optional: RedisInsight for UI

```bash
docker run -d -p 8001:8001 --name redis-insight \
  --link dev-redis:redis \
  redis/redisinsight:latest
```

Access at: [http://localhost:8001](http://localhost:8001)

---

## 🧪 Testing Without Redis

Use `fakeredis` as a memory backend for tests/dev:

```env
RATE_LIMIT_BACKEND=LOCAL
```

---

## 🧠 Best Practices

- ✅ Use token-based keys for user-based throttling
- ✅ Apply stricter limits on sensitive routes like `/login`, `/register`
- ✅ Always return `Retry-After` to guide clients
- ✅ Use namespaces or DB separation in Redis for staging vs prod

---

## 📚 References

- 📘 [fastapi-limiter GitHub](https://github.com/long2ice/fastapi-limiter)
- 📘 [Redis Docs](https://redis.io/docs/)
- 📘 [RedisInsight UI](https://redis.com/redis-enterprise/redis-insight/)
