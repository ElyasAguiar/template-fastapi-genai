"""Initialize and expose available tools for the agent."""

from langchain_core.tools import BaseTool

from .tavily_search_tool import TAVILY_SEARCH_TOOL

TOOLS: list[BaseTool] = [TAVILY_SEARCH_TOOL]

__all__ = ["TOOLS", "TAVILY_SEARCH_TOOL"]
