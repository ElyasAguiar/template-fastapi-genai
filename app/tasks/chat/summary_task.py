"""Celery task for generating a simple text summary."""

from app import celery_app


@celery_app.task(name="generate_summary")
def generate_summary(text: str) -> str:
    """Dummy summary generator task."""

    if not text:
        return "No content to summarize."

    # Placeholder summary logic
    summary = text[:100] + "..." if len(text) > 100 else text
    return f"Summary: {summary}"
