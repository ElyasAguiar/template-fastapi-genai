"""Graph schema for the LangGraph-based application."""

import operator
from typing import Annotated, Dict, List, TypedDict

from langchain_core.messages import BaseMessage, HumanMessage


class AgentState(TypedDict):
    """The state of the agent throughout the reasoning process."""

    question: HumanMessage
    refined_question: str
    require_enhancement: bool
    refined_questions: List[str]
    search_results: List[Dict]
    messages: Annotated[List[BaseMessage], operator.add]
