"""Question enhancement component for generating multiple refined websearch questions."""

from typing import Dict

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from loguru import logger
from pydantic import BaseModel, Field, SecretStr

from app import settings

from ..model_map import LLMModelMap
from ..states import AgentState


class EnhancedQuestionsResult(BaseModel):
    """
    Output schema representing multiple refined questions derived from the original query,
    aimed at maximizing the breadth and precision of a web search.
    """

    refined_questions: list[str] = Field(
        description="List of enhanced, standalone refined_questions for web search. Should include exactly 2 distinct and optimized questions."
    )


class QuestionEnhancer:
    """Agent component responsible for expanding a single query into multiple precise search questions."""

    def __init__(self):
        self.llm = ChatOpenAI(
            model=LLMModelMap.QUESTION_ENHANCER,
            api_key=SecretStr(settings.OPENAI_API_KEY),
        ).with_structured_output(
            schema=EnhancedQuestionsResult,
            strict=True,
        )

    def enhance(self, state: AgentState) -> Dict:
        """
        Enhances a question into multiple standalone questions for better web search coverage.
        """

        question = (
            state["refined_question"]
            if state.get("refined_question")
            else state["question"].content
        )

        conversation = [
            SystemMessage(
                content=(
                    "You are a helpful assistant that rewrites a single complex question "
                    "into two standalone, web-search-friendly questions for broader and more precise retrieval."
                )
            ),
            HumanMessage(content=question),
        ]

        enhancer_prompt = ChatPromptTemplate.from_messages(conversation)

        logger.info(f"Prompt constructed for enhancement: {enhancer_prompt}")

        response_data = (enhancer_prompt | self.llm).invoke({})
        response = EnhancedQuestionsResult.model_validate(response_data)

        logger.info(f"Generated enhanced questions: {response.refined_questions}")

        return {"refined_questions": response.refined_questions}
