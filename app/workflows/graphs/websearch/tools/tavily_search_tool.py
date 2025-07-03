"""Tavily search tool for websearch."""

from langchain_core.tools import BaseTool
from langchain_tavily import TavilySearch

from app import settings

TAVILY_SEARCH_TOOL: BaseTool = TavilySearch(
    max_results=10,
    topic="general",
    include_answer=False,
    include_raw_content=False,
    include_images=False,
    include_image_descriptions=False,
    search_depth="basic",
    time_range="day",
    include_domains=None,
    exclude_domains=None,
    country=None,
    tavily_api_key=settings.TAVILY_API_KEY,
)
