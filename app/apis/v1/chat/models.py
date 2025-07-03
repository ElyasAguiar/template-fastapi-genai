"""Request module for chat streaming API."""

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """Request model for configuring chat token streaming."""

    sleep: float = Field(
        1,
        json_schema_extra={
            "description": "Sleep duration (in seconds) between streamed tokens."
        },
    )
    number: int = Field(
        10, json_schema_extra={"description": "Total number of tokens to stream."}
    )


class WebSearchChatRequest(BaseModel):
    """Request model for initiating a web search-based chat response."""

    question: str = Field(
        description="The user's input question to be processed for web search and answer generation."
    )
    thread_id: str = Field(
        description="Unique identifier for the chat thread to maintain context across requests."
    )


class SummaryRequest(BaseModel):
    """Request model for submitting text to the summary task."""

    text: str = Field(
        ..., json_schema_extra={"description": "The text content to summarize."}
    )
