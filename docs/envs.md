# 🌍 Environment Variables

Application configuration is fully managed through a `.env` file using `pydantic.BaseSettings`. This approach ensures environment-specific settings can be easily managed without hardcoding values.

---

## ✅ Sample `.env`

```env
# App Environment
ENVIRONMENT=development         # Options: development | qa | demo |production
LOG_LEVEL=DEBUG                 # Options: TRACE| DEBUG | INFO | WARNING | ERROR

# Server Configuration
HOST=0.0.0.0
PORT=8002
WORKER_COUNT=4

# Redis Configuration
REDIS_HOST=redis
REDIS_PORT=6379
REDIS_PASSWORD=yourStrongPassword

# Grafana Configuration
GF_SECURITY_ADMIN_USER=admin
GF_SECURITY_ADMIN_PASSWORD=supersecurepassword
```

---

## ⚙️ How It Works

These values are automatically loaded into your application via `pydantic.BaseSettings`. This allows seamless environment variable parsing with type validation and default fallback support.

---

## 🔒 Best Practices

* Do **not** commit your `.env` file to version control.
* Use `.env.sample` to share required variables with your team.
* For production, prefer secret management tools (e.g., Docker secrets, AWS SSM, HashiCorp Vault) over plain-text `.env`.
