"""Configuration settings for the application"""

import enum
from typing import Union

from pydantic_settings import BaseSettings, SettingsConfigDict


class LogLevel(str, enum.Enum):
    """Defines available logging levels for application monitoring and debugging."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"
    TRACE = "TRACE"


class CacheBackend(str, enum.Enum):
    """Supported cache backends."""

    REDIS = "redis"
    LOCAL = "local"


class RateLimitBackend(str, enum.Enum):
    """Supported rate-limit backends."""

    REDIS = "redis"
    LOCAL = "local"


class AppEnvs(str, enum.Enum):
    """Application envs"""

    DEVELOPMENT = "development"
    QA = "qa"
    DEMO = "demo"
    PRODUCTION = "production"


class AppConfig(BaseSettings):
    """Primary configuration settings for the application."""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    LOG_LEVEL: LogLevel = LogLevel.TRACE
    RELEASE_VERSION: str = "0.0.1"
    ENVIRONMENT: AppEnvs = AppEnvs.DEVELOPMENT
    HOST: str = "0.0.0.0"
    PORT: int = 8002
    WORKER_COUNT: Union[int, None] = None

    # Cache
    CACHE_BACKEND: CacheBackend = CacheBackend.LOCAL

    # Rate Limit
    RATE_LIMIT_BACKEND: RateLimitBackend = RateLimitBackend.REDIS

    # Redis
    REDIS_HOST: str = ""
    REDIS_PORT: str = ""
    REDIS_PASSWORD: str = ""

    # OPENAI Model
    OPENAI_API_KEY: str = ""
    TAVILY_API_KEY: str = ""

    # LangFuse
    LANGFUSE_HOST: str = ""
    LANGFUSE_PUBLIC_KEY: str = ""
    LANGFUSE_SECRET_KEY: str = ""


# Initialize configuration settings
settings = AppConfig()
