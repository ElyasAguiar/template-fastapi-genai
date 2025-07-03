<h1 align="center">🚀 FASTAPI-GENAI-BOILERPLATE</h1>

<p align="center">
  <i>Accelerate Innovation with Seamless AI-Driven APIs</i>
</p>

<p align="center">
  <img src="https://img.shields.io/github/last-commit/kevaldekivadiya2415/fastapi-genai-boilerplate?style=flat-square&cacheBust=1" />
  <img src="https://img.shields.io/github/languages/top/kevaldekivadiya2415/fastapi-genai-boilerplate?style=flat-square&cacheBust=1" />
  <img src="https://img.shields.io/github/languages/count/kevaldekivadiya2415/fastapi-genai-boilerplate?style=flat-square&cacheBust=1" />
  <img src=https://img.shields.io/badge/Python-3.9%20|%203.10%20|%203.11%20|%203.12%20|%203.13-blue?style=flat-square&logo=python />
</p>

---

<p align="center">
  <i>Powered by industry-grade technologies</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Markdown-000000?logo=markdown&logoColor=white&style=flat-square" />
  <img src="https://img.shields.io/badge/TOML-9c4221?logo=toml&logoColor=white&style=flat-square" />
  <img src="https://img.shields.io/badge/Pre--commit-orange?logo=pre-commit&logoColor=white&style=flat-square" />
  <img src="https://img.shields.io/badge/Ruff-ccff00?logo=ruff&logoColor=black&style=flat-square" />
  <img src="https://img.shields.io/badge/GNU%20Bash-89e051?logo=gnubash&logoColor=white&style=flat-square" />
  <br/>
  <img src="https://img.shields.io/badge/Gunicorn-499848?logo=gunicorn&logoColor=white&style=flat-square" />
  <img src="https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white&style=flat-square" />
  <img src="https://img.shields.io/badge/Docker-2496ed?logo=docker&logoColor=white&style=flat-square" />
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=flat-square" />
  <img src="https://img.shields.io/badge/uv-55BB8E?logo=python&logoColor=white&style=flat-square" />
  <img src="https://img.shields.io/badge/Redis-DC382D?logo=redis&logoColor=white&style=flat-square" />
  <img src="https://img.shields.io/badge/LangChain-ffffff?logo=langchain&logoColor=green" />
  <img src="https://img.shields.io/badge/LangGraph-ffffff?style=flat-square&color=3b82f6" />
  <img src="https://img.shields.io/badge/Langfuse-ffffff?style=flat-square&color=00A8E8" />


</p>

---

> 🚀 **Why This Boilerplate?**
>
> Most FastAPI AI boilerplates lack production-readiness and multi-agent capabilities.
>
> This project solves that with:
> 
> - 🧩 Modular architecture for **multiple LangGraph workflows**, agents, and pipelines  
> - 🔍 Integrated **Langfuse tracing** for debugging & observability  
> - 🐳 **Production-ready** deployment using Docker + Gunicorn  
> - 🧠 Optimized for **AI workflow orchestration** and scalable GenAI apps  
>
> 📘 **For in-depth documentation**, visit the [`/docs`](./docs) folder.

---

## 📂 Table of Contents

- [Overview](#-overview)
- [What Makes It Stand Out](#-what-makes-it-stand-out)
- [Tech Stack](#-tech-stack)
- [Folder Structure](#-folder-structure)
- [Getting Started](#-getting-started)
- [Makefile Commands](#-makefile-commands)
- [Pre-commit Hooks](#-pre-commit-hooks)
- [Logging Middleware](#-logging-middleware)
- [Configuration](#-configuration)
- [Testing & Linting](#-testing--linting)
- [Deployment](#-deployment)
- [Monitoring with Prometheus & Grafana](#-monitoring-with-prometheus--grafana)
- [Redis Caching](#-redis-caching)
- [Docker Compose Setup](#-docker-compose-setup)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)

---

## 📘 Overview

**`fastapi-genai-boilerplate`** is a scalable and production-ready starter template for building FastAPI applications with modern DevOps practices. It supports:

- Environment-aware configuration
- Observability (logging, tracing)
- Security (rate limiting)
- Maintainability (typed config, modular API)
- CI-ready with code quality hooks and Docker support

---

## 🌟 What Makes It Stand Out

This template empowers you to build robust, scalable, and maintainable APIs with:

- 🌐 **Environment-aware Config**
  Seamlessly toggle between development and production settings for streamlined deployments.

- 🔎 **Request Tracing & Logging**
  Full observability using `loguru`, with structured logs, X-Request-ID headers, and performance metrics.

- 🛡️ **Rate Limiting Middleware**
  Protect endpoints from abuse using `fastapi-limiter`, based on identity/IP-based throttling.

- 🐳 **Dockerized Deployment**
  Container-first architecture with clean Dockerfile and production startup scripts using Gunicorn + Uvicorn.

- 🚀 **Production Server Setup**
  Efficient worker scaling with CPU-aware concurrency, custom Makefile for simplified operations.

- 🧩 **Modular API Architecture**
  Clean separation of concerns with well-defined folder structure, ready for features like chat, auth, etc.

---

## 🧪 Tech Stack

| Category         | Tools |
|------------------|-------|
| Core Framework   | [FastAPI](https://fastapi.tiangolo.com/) |
| ASGI Servers     | [Uvicorn](https://www.uvicorn.org/), [Gunicorn](https://gunicorn.org/) |
| Dependency Mgmt  | [UV](https://docs.astral.sh/uv/) |
| Configuration    | [Pydantic](https://pydantic.dev/) |
| Logging          | [Loguru](https://loguru.readthedocs.io/) |
| Rate Limiting    | [FastAPI-Limiter](https://github.com/long2ice/fastapi-limiter) |
| Linting/Checks   | [Ruff](https://beta.ruff.rs/), [Black](https://black.readthedocs.io/), [MyPy](https://mypy-lang.org/), [isort](https://pycqa.github.io/isort/) |
| CI & Hooks       | [pre-commit](https://pre-commit.com/) |
| Containerization | [Docker](https://www.docker.com/) |

---

## 🗂️ Folder Structure

```
fastapi_genai_boilerplate/
├── app/
│   ├── api/                     # API routes and handlers
│   ├── core/
│   │   ├── config.py            # App settings and environment config
│   │   └── middlewares/         # Logging, rate limit middleware
│   └── main.py                  # App bootstrap logic
├── tests/                       # Test cases
├── .env                         # Local environment variables
├── Dockerfile                   # Docker setup
├── Makefile                     # Developer shortcuts
├── pyproject.toml               # UV dependencies & configs
├── pre-commit-config.yaml       # Git hook configs
└── README.md                    # Project documentation
```

---

## ⚙️ Getting Started

### 1. Clone & Install Dependencies

```bash
# Clone the repository
git clone https://github.com/kevaldekivadiya2415/fastapi-genai-boilerplate
cd fastapi-genai-boilerplate

# Optional: create and activate virtual environment (recommended)
uv venv
source .venv/bin/activate

# Install uv via pip
pip3 install uv

# Sync dependencies from pyproject.toml and uv.lock
uv sync

# Start an interactive Python shell with uv
uv run main.py
```

### 2. Add a `.env` File

```env
LOG_LEVEL=DEBUG
ENVIRONMENT=development
HOST=0.0.0.0
PORT=8002
WORKER_COUNT=4
```

---

## 🛠️ Makefile Commands

| Command                   | Description                            |
|---------------------------|----------------------------------------|
| `make run-dev`            | Start dev server with auto-reload      |
| `make run-prod`           | Start Gunicorn server with Uvicorn     |
| `make lint`               | Run `ruff` linter                      |
| `make typecheck`          | Run static type checks with MyPy       |
| `make format`             | Format using Black & isort             |
| `make docker-build`       | Build Docker image                     |
| `make docker-run`         | Run Docker container                   |
| `make pre-commit-install` | Install all Git pre-commit hooks       |

---

## ✅ Pre-commit Hooks

Enforce standards before every commit. Tools include:

- ✅ `ruff` for linting
- ✅ `black` for formatting
- ✅ `isort` for import order
- ✅ `mypy` for type checks

Install hooks:

```bash
make pre-commit-install
```

---

## 📊 Logging Middleware

Each request gets a unique ID:

- Injected via `X-Request-ID` header
- Auto-generated if missing
- Passed into log messages using `loguru`
- Added in response header for traceability

Ideal for debugging and log correlation across microservices.

---

## 🔧 Configuration

All environment values are type-safe using `pydantic.BaseSettings`.
Defaults can be overridden via `.env` file.

```python
class AppConfig(BaseSettings):
    LOG_LEVEL:syr = LogLevel.TRACE
    RELEASE_VERSION: str = "0.0.1"
    ENVIRONMENT: str = AppEnvs.DEVELOPMENT
    HOST: str = "0.0.0.0"
    PORT: int = 8002
    WORKER_COUNT: Union[int, None] = None

    # Redis
    REDIS_HOST: str = ""
    REDIS_PORT: str = ""
    REDIS_PASSWORD: str = ""
```

---

## 🧪 Testing & Linting

Run checks with:

```bash
make lint
make typecheck
make format
```

Use `pytest` (not included yet) for writing unit/integration tests inside `tests/`.

---

## 🚀 Deployment

### Docker Deployment:

```bash
make docker-build
make docker-run
```

Production uses:

- `Gunicorn` with `UvicornWorker`
- `.env` to control concurrency

---

## 📊 Monitoring with Prometheus & Grafana

This boilerplate includes built-in observability via the `prometheus-fastapi-instrumentator` library.

### 🔧 Metrics Endpoint

All FastAPI metrics (latency, requests, status codes, etc.) are exposed at:

```http://HOST:PORT/metrics```

---

## 🐳 Docker Compose Setup

A `docker-compose.yml` file is included to run the full observability stack:

* ✅ FastAPI App
* 📊 Prometheus (for metrics collection)
* 📈 Grafana (for dashboards)
* 🧠 Redis (for caching and Celery task queue)
* 🧰 RedisInsight (for Redis GUI)

### ▶️ Usage

Run everything with:

```bash
docker-compose up --build
```

### 📍 Port Mapping Overview

| Service       | URL                                              | Host Port | Container Port |
| ------------- | ------------------------------------------------ | --------- | -------------- |
| FastAPI       | [http://localhost:8002](http://localhost:8002)   | `8002`    | `8002`         |
| Prometheus    | [http://localhost:9091](http://localhost:9091)   | `9091`    | `9091`         |
| Grafana       | [http://localhost:3000](http://localhost:3000)   | `3000`    | `3000`         |
| RedisInsight  | [http://localhost:8001](http://localhost:8001)   | `8001`    | `8001`         |


### 🔐 Grafana Credentials
By default, Grafana uses the following login credentials (configured via environment variables):

```
Username: admin
Password: supersecurepassword
```

You can modify these in the ```docker-compose.yml``` under the grafana service:
```
grafana:
  image: grafana/grafana
  ports:
    - "3000:3000"
  environment:
    - GF_SECURITY_ADMIN_USER=admin
    - GF_SECURITY_ADMIN_PASSWORD=supersecurepassword
```

### 🗂️ Prometheus Configuration

Make sure the following file exists:

```
docker/
└── prometheus/
    └── prometheus.yml
```

Example:

```yaml
# docker/prometheus/prometheus.yml

global:
  scrape_interval: 5s

scrape_configs:
  - job_name: 'fastapi'
    metrics_path: /metrics
    static_configs:
      - targets: ['fastapi:8002']
```

> 🔁 Prometheus scrapes `/metrics` from FastAPI every 5 seconds.

---

## 🧠 Redis Caching

This boilerplate uses **Redis with `aiocache`** for request-level caching and task results.

### ✅ Features

* Uses **Redis** as the cache backend
* JSON serialization of values
* TTL (Time-To-Live) support
* Namespace isolation
* Authentication support (username/password)

### ⚙️ Redis Cache Configuration

Caching is set up in `app/core/cache/cache.py`:

```python
from aiocache import Cache
from aiocache.serializers import JsonSerializer
from app.core.config import settings

cache = Cache(
    cache_class=Cache.REDIS,  # Redis backend
    endpoint=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    username=settings.REDIS_USER,
    password=settings.REDIS_PASSWORD,
    ttl=300,  # Cache timeout in 300 seconds (5 mins)
    namespace="fastapi_cache",
    serializer=JsonSerializer(),
    db=1,
)
```

### 🛡️ Brute Force Protection Tip

To prevent cache pollution by brute-force query changes:

* Normalize/cache keys using request fingerprinting
* Apply rate-limiting middleware (already included via `fastapi-limiter`)
* Use checksum-based cache keys (e.g. `hashlib.sha256(json.dumps(payload))`)

### 📦 Docker Redis Setup

Redis (with RedisInsight UI) is exposed via Docker:

| Service      | URL                                            | Host Port | Container Port |
| ------------ | ---------------------------------------------- | --------- | -------------- |
| Redis        | redis://localhost:6379                        | `6379`    | `6379`         |
| RedisInsight | [http://localhost:8001](http://localhost:8001) | `8001`    | `8001`         |

---

### ⛔ To Stop Everything

```bash
docker-compose down
```

---

## 📊 Langfuse Integration

This boilerplate is compatible with [Langfuse](https://www.langfuse.com/) for observability, tracing, and debugging of LLM-based applications.

### ✅ Features

* Trace all API interactions and GenAI requests
* View detailed logs, timings, metadata, and user sessions
* Works with OpenAI, Anthropic, HuggingFace, and custom model providers

### ⚙️ Setup Instructions

1. **Start Langfuse via Docker Compose**

   ```bash
   docker compose -f docker-compose-langfuse.yaml up -d
   ```

2. **Access the Langfuse UI**

   Open your browser at [http://localhost:3000](http://localhost:3000)

3. **Sign Up & Create Project**

   * Register your admin user
   * Create a new project
   * Copy the **Public** and **Secret** API keys

4. **Add Langfuse Credentials to `.env`**

   ```env
   LANGFUSE_HOST=http://localhost:3000
   LANGFUSE_PUBLIC_KEY=your-public-key-here
   LANGFUSE_SECRET_KEY=your-secret-key-here
   ```
---

## 🧩 Documentation

- 🧠 [Logging Middleware](docs/logging.md)
- 🛠️ [Makefile Commands](docs/makefile.md)
- 🌍 [Environment Variables](docs/envs.md)
- 🐳 [Docker Compose Setup](docs/docker-compose.md)
- 🛡️ [Rate Limiting with FastAPI-Limiter](docs/rate_limit.md)
- 🧭 [Trace Decorator](docs/trace.md)
- 📊 [Langfuse Integration Guide](docs/langfuse.md)
---

## 🤝 Contributing

You're welcome to contribute! Please:

1. Fork this repo
2. Create a new branch
3. Ensure pre-commit and linters pass
4. Open a PR with a clear description

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](./LICENSE) file for details.

---

[![Star History Chart](https://api.star-history.com/svg?repos=kevaldekivadiya2415/fastapi-genai-boilerplate&type=Date)](https://star-history.com/#kevaldekivadiya/fastapi-genai-boilerplate&Date)
