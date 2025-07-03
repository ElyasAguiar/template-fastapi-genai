"""This file contains the prompts for the agent."""

from pathlib import Path

from loguru import logger


def load_prompt(prompt_filename: str) -> str:
    """Load and format a prompt from a markdown file."""
    prompt_path = Path(__file__).parent / prompt_filename

    if not prompt_path.exists():
        logger.critical(f"Missing required prompt file: {prompt_path}")
        raise FileNotFoundError(f"Prompt file not found: {prompt_path}")

    try:
        raw_prompt = prompt_path.read_text(encoding="utf-8")
        return raw_prompt

    except Exception:
        logger.critical("Failed to load or format the prompt.", exc_info=True)
        raise


SYSTEM_PROMPT = load_prompt("system.md")
RAG_PROMPT = load_prompt("rag.md")
