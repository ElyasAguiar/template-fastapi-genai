# Project Metadata
PROJECT_NAME := fastapi_boilerplate
ENV_FILE := ".env"
PORT := $(shell grep ^PORT= $(ENV_FILE) | cut -d '=' -f2)

# Commands
PYTHON := uv run python
UVICORN := $(PYTHON) main.py
ISORT := uv run isort .
BLACK := uv run black .
RUFF := uv run ruff .
MYPY := uv run mypy .
PRECOMMIT := uv run pre-commit

# Default
.DEFAULT_GOAL := help

## ----------- Local Development -----------

.PHONY: run
run: ## Run FastAPI app with reload (Dev)
	$(UVICORN) --reload --env-file $(ENV_FILE)

.PHONY: start
start: ## Run FastAPI app for production
	$(UVICORN) --env-file $(ENV_FILE)

.PHONY: shell
shell: ## Open Python shell in uv env
	$(PYTHON)

## ----------- Linting & Formatting -----------

.PHONY: format
format: ## Format code with black and isort
	$(ISORT)
	$(BLACK)

.PHONY: lint
lint: ## Run linters (ruff + mypy)
	uv pip run ruff check .
	$(MYPY)

.PHONY: check
check: ## Run pre-commit on all files
	$(PRECOMMIT) run --all-files

.PHONY: install-hooks
install-hooks: ## Install pre-commit hooks
	$(PRECOMMIT) install

## ----------- Testing -----------

.PHONY: test
test: ## Run tests
	@echo "No tests defined yet."

## ----------- Utilities -----------

.PHONY: clean
clean: ## Clean __pycache__ and .pytest_cache
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf .pytest_cache .mypy_cache .ruff_cache

.PHONY: help
help: ## Show help info
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-18s\033[0m %s\n", $$1, $$2}'

## ----------- Docker -----------

.PHONY: docker-build
docker-build: ## Build the docker image for the project
	docker build -t $(PROJECT_NAME):latest .

.PHONY: docker-run
docker-run: ## Run the docker container from the image
	docker run --rm -p ${PORT}:${PORT} $(PROJECT_NAME):latest
