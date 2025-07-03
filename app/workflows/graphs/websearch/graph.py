"""LangGraph agent graph setup using class-based node components."""

from langfuse import Langfuse, get_client
from langfuse.langchain import CallbackHandler
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, StateGraph

from app import settings

from .components.answer_generator import AnswerGenerator
from .components.conditional_edges import route_after_question_rewrite
from .components.question_enhancer import QuestionEnhancer
from .components.question_rewriter import QuestionRewriter
from .components.websearch_executor import WebSearchExecutor
from .states import AgentState

checkpointer = InMemorySaver()
Langfuse(
    public_key=settings.LANGFUSE_PUBLIC_KEY,
    secret_key=settings.LANGFUSE_SECRET_KEY,
    host=settings.LANGFUSE_HOST,
)
langfuse = get_client()
langfuse_handler = CallbackHandler(public_key=settings.LANGFUSE_PUBLIC_KEY)


class WebSearchAgentGraph:
    """Encapsulates the LangGraph agent state workflow using class-based components."""

    def __init__(self):
        # Instantiate node components
        self.rewriter = QuestionRewriter()
        self.enhancer = QuestionEnhancer()
        self.searcher = WebSearchExecutor()
        self.answerer = AnswerGenerator()

        # Create the StateGraph
        self.workflow = StateGraph(AgentState)

        self._build()

    def _build(self):
        """Internal method to build the graph structure."""
        # Register functional nodes
        self.workflow.add_node("question_rewriter", self.rewriter.rewrite)
        self.workflow.add_node("question_enhancer", self.enhancer.enhance)
        self.workflow.add_node("websearch", self.searcher.search)
        self.workflow.add_node("answer_generation", self.answerer.generate)

        # Define flow
        self.workflow.set_entry_point("question_rewriter")
        self.workflow.add_edge("question_enhancer", "websearch")
        self.workflow.add_edge("websearch", "answer_generation")
        self.workflow.add_edge("answer_generation", END)

        # Conditional branching from question_rewriter
        self.workflow.add_conditional_edges(
            "question_rewriter",
            route_after_question_rewrite,
            {
                "question_enhancer": "question_enhancer",
                "websearch": "websearch",
            },
        )

    def compile(self):
        """Compile the LangGraph workflow with checkpointer."""
        return self.workflow.compile(checkpointer=checkpointer).with_config(
            {"callbacks": [langfuse_handler]}
        )
