## 🚀 Langfuse Docker Setup

This repository provides a production-ready `docker-compose-langfuse.yaml` configuration to self-host Langfuse along with the required services: PostgreSQL, ClickHouse, Redis, and MinIO.

---

### 📦 Prerequisites

Make sure you have the following installed:

* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)

---

### 🛠️ Configuration

Before running the services, you need to update some environment variables (marked as `# CHANGEME`) inside `docker-compose-langfuse.yaml`.

**Required values to update:**

* `DATABASE_URL`
* `ENCRYPTION_KEY`: Generate with `openssl rand -hex 32`
* `SALT`: Your own string salt
* `REDIS_AUTH`
* `MINIO_ROOT_PASSWORD`
* `CLICKHOUSE_PASSWORD`
* `NEXTAUTH_SECRET`
* `LANGFUSE_INIT_*`: Initialize org/project/user for Langfuse

---

### 🧪 Running Langfuse Locally

1. **Start services**

   ```bash
   docker-compose -f docker-compose-langfuse.yaml up --build -d
   ```

2. **Verify containers are running**

   ```bash
   docker ps
   ```

3. **Visit Langfuse dashboard**

   Open your browser and go to:

   ```
   http://localhost:3000
   ```

---

### 📁 Volumes

The following Docker volumes are created:

* `langfuse_postgres_data`
* `langfuse_clickhouse_data`
* `langfuse_clickhouse_logs`
* `langfuse_minio_data`

These persist data across container restarts.

---

### 🛑 Stopping & Cleaning Up

Stop the services:

```bash
docker-compose -f docker-compose-langfuse.yaml down
```

To also remove volumes:

```bash
docker-compose -f docker-compose-langfuse.yaml down -v
```

---

### 🧰 Useful Commands

* View logs:

  ```bash
  docker-compose -f docker-compose-langfuse.yaml logs -f
  ```

---

### 🧭 Next Steps: Sign Up and Save API Keys

Once the Langfuse UI is running at [http://localhost:3000](http://localhost:3000):

1. **Sign Up**

   * Visit [http://localhost:3000](http://localhost:3000)
   * Fill in your email, name, and password to register as the first admin user

2. **Create a Project**

   * After logging in, click **"New Project"**
   * Enter a name (e.g., `My AI App`) and click **"Create"**

3. **Get Your API Credentials**

   * After project creation, go to **Settings > API Keys**
   * Copy the **Public** and **Secret** keys

4. **Save in `.env` file**

```env
LANGFUSE_HOST=http://localhost:3000
LANGFUSE_PUBLIC_KEY=your-public-key-here
LANGFUSE_SECRET_KEY=your-secret-key-here
```

> ✅ These keys are required for Langfuse SDKs to send traces and usage data from your application.

### 📎 Resources

* 🌐 Langfuse Docs: [https://langfuse.com/docs](https://langfuse.com/docs)
* 🐳 Docker Docs: [https://docs.docker.com/](https://docs.docker.com/)
