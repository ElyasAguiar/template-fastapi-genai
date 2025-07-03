# 🐳 Docker Compose Setup

This project includes a full Docker Compose setup to spin up all core services required for development, testing, and monitoring.

---

### ▶️ Usage

```bash
docker-compose up --build
````

Use `-d` flag to run containers in detached mode:

```bash
docker-compose up --build -d
```

---

### 🔌 Included Services

* ✅ FastAPI application
* ⚙️ Celery worker (background tasks)
* 🧠 Redis (for cache & task queue)
* 📊 RedisInsight (visual Redis UI)
* 📈 Prometheus (metrics collection)
* 📉 Grafana (dashboard and visualization)
* 📦 Loki & Promtail (log aggregation and shipping)

---

### 🔐 Grafana Credentials

```text
Username: admin
Password: supersecurepassword
```

Update the credentials in your `.env` or `provisioning` files as needed.

---

### 📍 Port Mapping

| Service      | URL                                            | Port |
| ------------ | ---------------------------------------------- | ---- |
| FastAPI      | [http://localhost:8002](http://localhost:8002) | 8002 |
| RedisInsight | [http://localhost:8001](http://localhost:8001) | 8001 |
| Prometheus   | [http://localhost:9091](http://localhost:9091) | 9091 |
| Grafana      | [http://localhost:3000](http://localhost:3000) | 3000 |
| Loki         | [http://localhost:3100](http://localhost:3100) | 3100 |

---

> 💡 **Tip:**
> You can scale or manage individual services by modifying the `docker-compose.yml` and `.env` files as needed.

---

## 🔗 Reference Section for `README.md`

Update your main `README.md` to link the relevant documentation files like this:


## 🧩 Documentation

- 🧠 [Logging Middleware](docs/logging.md)
- 🛠️ [Makefile Commands](docs/makefile.md)
- 🌍 [Environment Variables](docs/envs.md)
- 🐳 [Docker Compose Setup](docs/docker-compose.md)
