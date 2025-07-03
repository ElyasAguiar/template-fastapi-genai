"""Chat service"""

import asyncio
import hashlib
import json
import re
from typing import Any, AsyncGenerator, Callable, Tuple

from celery.result import AsyncResult
from langchain_core.messages import AIMessageChunk, HumanMessage
from loguru import logger

from app import cache, celery_app, trace
from app.tasks.chat import generate_summary

from ....workflows.graphs.websearch import WebSearchAgentGraph
from .helper import CitationReplacer
from .models import ChatRequest, WebSearchChatRequest


class ChatService:
    """Service for handling chat logic."""

    def __init__(self) -> None:
        """Initialize the chat service."""
        pass

    @staticmethod
    def _hash_request(payload: dict) -> str:
        """Generate a unique cache key from request payload."""
        return hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()

    @trace(name="chat_service")
    async def chat_service(
        self, request_params: ChatRequest
    ) -> Callable[[], AsyncGenerator[str, None]]:
        """
        Return a streaming chat generator.
        If the response is cached, replay the cached stream.
        Otherwise, generate the stream and cache the result.
        """
        payload = request_params.model_dump()
        cache_key = self._hash_request(payload)
        logger.debug(f"Generated cache key: {cache_key}")

        cached_response = await cache.get(cache_key)
        if cached_response:
            logger.info("Cache hit. Replaying cached response.")

            async def replay_cached_stream() -> AsyncGenerator[str, None]:
                for chunk in cached_response.split("\n\n"):
                    yield chunk + "\n\n"

            return replay_cached_stream

        logger.info("Cache miss. Generating new response stream.")

        async def stream() -> AsyncGenerator[str, None]:
            buffer = ""
            for i in range(request_params.number):
                chunk = f"event: content\ndata: {i}\n\n"
                logger.debug(f"Streaming chunk: {chunk.strip()}")

                buffer += chunk
                yield chunk
                await asyncio.sleep(request_params.sleep)

            chunk = "event: complete\ndata: [DONE]\n\n"
            logger.debug("Streaming complete chunk.")
            buffer += chunk
            yield chunk

            await cache.set(cache_key, buffer)
            logger.info(f"Response cached under key: {cache_key}")

        return stream

    @trace(name="chat_websearch_service")
    async def chat_websearch_service(
        self, request_params: WebSearchChatRequest
    ) -> Callable[[], AsyncGenerator[str, None]]:
        """Handles streaming chat responses with integrated web search results."""

        # Compile the LangGraph agent
        graph = WebSearchAgentGraph().compile()

        # Prepare initial input for agent execution
        state_input = {
            "question": HumanMessage(content=request_params.question),
            "refined_question": "",
            "require_enhancement": False,
            "questions": [],
            "search_results": [],
            "messages": [HumanMessage(content=request_params.question)],
        }

        # Run the workflow and get the final state
        async def stream() -> AsyncGenerator[str, None]:
            raw_citation_map = {}
            superscript_buffer = ""
            replacer = CitationReplacer()

            for mode, chunk in graph.stream(
                input=state_input,
                config={"configurable": {"thread_id": str(request_params.thread_id)}},
                stream_mode=["messages", "custom"],
            ):
                if mode == "custom":
                    raw_citation_map.update(chunk.get("citation_map", {}))

                elif mode == "messages":
                    _chunk, metadata = chunk[0], chunk[1]
                    langgraph_node = metadata.get("langgraph_node")

                    if (
                        hasattr(_chunk, "content")
                        and _chunk.content
                        and langgraph_node == "answer_generation"
                        and isinstance(_chunk, AIMessageChunk)
                    ):
                        logger.debug(_chunk)

                        content = str(_chunk.content)

                        if replacer.is_superscript(content):
                            superscript_buffer += content
                            continue

                        if superscript_buffer:
                            content = superscript_buffer + content
                            superscript_buffer = ""

                        cleaned = re.sub(r"[⁰¹²³⁴⁵⁶⁷⁸⁹]+", replacer.replace, content)
                        yield f"event: content\ndata: {cleaned}\n\n"

            final_citation_map = {
                str(replacer.superscript_to_index[k]): raw_citation_map[k]
                for k in replacer.superscript_to_index
                if k in raw_citation_map
            }

            yield f"event: citation\ndata: {final_citation_map}\n\n"
            yield "event: complete\ndata: [DONE]\n\n"

        return stream

    async def submit_summary_task(self, text: str) -> Tuple[Any, str, int]:
        """Submit a summary task to Celery and return the task ID."""

        logger.info("Submitting summary task to Celery")
        task = generate_summary.delay(text)
        logger.debug(f"Summary task submitted. Task ID: {task.id}")

        return (
            {"task_id": task.id, "status": "submitted"},
            "Summary task has been successfully submitted.",
            200,
        )

    async def summary_status(self, task_id: str) -> Tuple[Any, str, int]:
        """Check the status of a summary task and return the result if available."""

        result = AsyncResult(task_id, app=celery_app)

        response_data = {
            "task_id": task_id,
            "status": result.status,
        }

        # Only include result if it's ready
        if result.ready():
            response_data["result"] = result.result

        return (
            response_data,
            "Summary task status retrieved successfully.",
            200,
        )
