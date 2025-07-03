# 🧠 Flexible Caching with aiocache

This project supports both **Redis** and **in-memory** caching backends via `aiocache`. It enables request-level caching, background task result storage, and general performance boosts with minimal effort.

---

## ✅ Features

* 🔄 **Pluggable cache backend** (Redis or in-memory)
* 📦 **JSON serialization**
* 🕒 **TTL (Time-to-Live)** support
* 🧱 **Namespace isolation**
* 🔐 **Password-protected Redis support**
* ⚡ Fully async + compatible with FastAPI

---

## ⚙️ Configuration

Caching is configured in `app/core/cache/cache.py` using the `CacheBackend` enum:

```python
"""Simple cache setup using aiocache with support for Redis and in-memory backends."""

from aiocache import Cache
from aiocache.serializers import JsonSerializer

from app.core.config import settings
from app.core.enums import CacheBackend

if settings.CACHE_BACKEND == CacheBackend.REDIS:
    cache = Cache(
        cache_class=Cache.REDIS,  # type: ignore
        endpoint=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        password=settings.REDIS_PASSWORD,
        ttl=300,
        namespace="fastapi_cache",
        serializer=JsonSerializer(),
        db=1,
    )
elif settings.CACHE_BACKEND == CacheBackend.LOCAL:
    cache = Cache(
        cache_class=Cache.MEMORY,
        ttl=300,
        namespace="fastapi_cache",
        serializer=JsonSerializer(),
    )
else:
    raise ValueError(f"Unsupported cache backend: {settings.CACHE_BACKEND}")
```

---

## 🧾 .env Configuration

Make sure to set up the `.env` file accordingly:

```env
# General Cache Backend
CACHE_BACKEND=redis  # or "local"

# Redis Configuration
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=yourpassword
```

---

## 🔐 Security Best Practices

* Enable **password authentication** on production Redis servers
* Use **namespaces** to isolate cache domains
* Normalize or hash cache keys to prevent brute-force key flooding:
  ```python
  import hashlib

  def hashed_key(raw_key: str) -> str:
      return hashlib.sha256(raw_key.encode()).hexdigest()
  ```

---

## 🐳 Docker Redis Setup

The project includes Redis and RedisInsight for local development in `docker-compose.yml`:

| Service      | URL                                            | Port |
| ------------ | ---------------------------------------------- | ---- |
| Redis        | redis://localhost:6379                         | 6379 |
| RedisInsight | [http://localhost:8001](http://localhost:8001) | 8001 |

---

## 🧪 Sample Usage

```python
from app.core.cache.cache import cache

@router.get("/cached")
async def get_cached_response():
    result = await cache.get("my_cache_key")
    if result:
        return {"cached": True, "data": result}

    result = expensive_function()
    await cache.set("my_cache_key", result)
    return {"cached": False, "data": result}
```

---

## 📚 References

* [aiocache Docs](https://aiocache.readthedocs.io/)
* [RedisInsight](https://redis.com/redis-enterprise/redis-insight/)
* [FastAPI Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/)
