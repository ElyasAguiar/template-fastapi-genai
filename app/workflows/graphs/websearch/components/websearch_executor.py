"""Web search component that retrieves search results for enhanced or rephrased questions."""

from typing import Any, Dict, List

from loguru import logger

from ..states import AgentState
from ..tools import TAVILY_SEARCH_TOOL


class WebSearchExecutor:
    """Agent component responsible for executing web searches based on refined or enhanced questions."""

    def __init__(self):
        pass

    def search(self, state: AgentState) -> Dict[str, List[Dict[str, Any]]]:
        """
        Executes web search queries using available questions in the state.
        """
        questions = (
            state["refined_questions"]
            if state["refined_questions"]
            else [state["refined_question"]]
        )
        results = []

        for query in questions:
            logger.info(f"Performing web search for: {query}")
            result = TAVILY_SEARCH_TOOL.invoke({"query": query})

            for item in result.get("results"):
                if item.get("content"):
                    results.append(item)

        logger.info(f"Web search completed with {len(results)} result sets.")

        return {"search_results": results}
