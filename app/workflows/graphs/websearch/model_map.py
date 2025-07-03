"""Mapping of tasks to their corresponding LLM model names."""

import enum


class LLMModelMap(str, enum.Enum):
    """Enum mapping specific agent tasks to their respective LLM model identifiers."""

    QUESTION_REWRITER = "gpt-4.1-mini"
    QUESTION_ENHANCER = "gpt-4.1-mini"
    ANSWER_GENERATOR = "gpt-4.1-mini"
