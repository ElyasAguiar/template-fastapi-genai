"""Initialize the chat route Celery tasks."""

from .summary_task import generate_summary

__all__ = ["generate_summary"]
