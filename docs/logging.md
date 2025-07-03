# 📝 Logging Middleware

The logging middleware provides structured and traceable logs for each request.

### 🔐 Features
- Every request is tagged with a unique `X-Request-ID`
- Uses [Loguru](https://loguru.readthedocs.io/) for beautiful, asynchronous, and rich logs
- Middleware automatically appends log context for better observability

### ✨ Example
```http
GET /health
X-Request-ID: 123abc
````

```json
{"time": "2025-06-22T10:00:00", "level": "INFO", "message": "Handled /health", "request_id": "123abc"}
```
