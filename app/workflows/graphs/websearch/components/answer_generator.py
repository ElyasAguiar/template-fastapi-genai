"""Answer generation component using web search content and rephrased user question."""

from datetime import datetime
from typing import Dict, List

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langgraph.config import get_stream_writer
from loguru import logger
from pydantic import SecretStr

from app import settings

from ..model_map import LLMModelMap
from ..prompts import RAG_PROMPT, SYSTEM_PROMPT
from ..states import AgentState


class AnswerGenerator:
    """Agent component responsible for synthesizing a final answer from retrieved web content."""

    def __init__(self):
        self.llm = ChatOpenAI(
            model=LLMModelMap.ANSWER_GENERATOR,
            api_key=SecretStr(settings.OPENAI_API_KEY),
        )

    def generate(self, state: AgentState) -> Dict[str, List[AIMessage]]:
        """Generates an answer using retrieved web content and the user's refined question."""

        web_results = state["search_results"]
        result_blocks = {}
        combined_content = ""

        cnt = 1
        for result in web_results:
            content = result.get("content")
            if content is not None:
                result_blocks[str(cnt)] = result
                cnt += 1

        for key, result in result_blocks.items():
            content = result.get("content", "").strip()
            combined_content += f"{key}. {content}\n\n"

        # Stream citation
        writer = get_stream_writer()
        writer({"citation_map": result_blocks})

        rag_prompt = RAG_PROMPT.format(
            context=combined_content, question=state["question"].content
        )
        logger.debug(f"Aggregated content for answer generation:\n{rag_prompt}")

        # Prepare conversation history
        conversation = state["messages"][:-1] if len(state["messages"]) > 1 else []
        conversation.insert(
            0,
            SystemMessage(
                content=SYSTEM_PROMPT.format(
                    current_date_and_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )
            ),
        )
        conversation.append(HumanMessage(content=rag_prompt))
        prompt = ChatPromptTemplate.from_messages(conversation)

        logger.info(f"Prompt constructed for answer generation: {prompt}")
        answer = self.llm.invoke(prompt.format())
        logger.info(f"Final Answer Generated:\n{answer.content}")

        return {"messages": [AIMessage(content=answer.content)]}
