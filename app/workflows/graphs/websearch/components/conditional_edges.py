"""Conditional router for branching after question rewriting."""

from loguru import logger

from ..states import AgentState


def route_after_question_rewrite(state: AgentState) -> str:
    """Routes to the next node based on whether the question requires enhancement."""
    logger.debug("Entering `route_after_question_rewrite` decision function.")

    enhancement_required = (
        str(state.get("require_enhancement", "false")).lower() == "true"
    )

    if enhancement_required:
        logger.info("Routing to: question_enhancer")
        return "question_enhancer"
    else:
        logger.info("Routing to: websearch")
        return "websearch"
