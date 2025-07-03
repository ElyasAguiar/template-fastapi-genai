# 🛠️ Makefile Documentation

Speed up your development workflow with these predefined `make` commands. Each command simplifies common tasks, ensuring consistency and reducing manual effort across the team.

---

## 📋 Available Commands

### ▶️ `make run-dev`

**Start the development server**
Launches the FastAPI app with auto-reload enabled for local development.

---

### 🚀 `make run-prod`

**Start the production server**
Runs the application using Gunicorn with Uvicorn workers, suitable for production deployment.

---

### 🧹 `make lint`

**Lint the codebase**
Uses `ruff` to check for style violations, unused imports, and other common issues.

---

### 🔍 `make typecheck`

**Run type checks**
Performs static type checking with MyPy to catch bugs and type inconsistencies early.

---

### 🧼 `make format`

**Format the code**
Automatically formats the code using `black` and organizes imports with `isort` to maintain a clean codebase.

---

### 🐳 `make docker-build`

**Build the Docker image**
Constructs the Docker image for containerizing the application.

---

### 🐳 `make docker-run`

**Run the Docker container**
Starts the application inside a Docker container with default configuration.

---

### 🧩 `make pre-commit-install`

**Install Git pre-commit hooks**
Sets up pre-commit hooks to enforce code quality checks automatically before each commit.

---

### 🆘 `make help`

**List all available commands**
Displays a list of all supported `make` targets with descriptions.

---

## ✅ Recommended Workflow

1. Use `make pre-commit-install` after cloning the repo.
2. Use `make run-dev` during development.
3. Before committing:

   * Run `make format`
   * Run `make lint`
   * Run `make typecheck`
4. Use `make run-prod` or Docker commands for staging/production.
