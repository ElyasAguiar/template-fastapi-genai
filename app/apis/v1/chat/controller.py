"""Route for chat streaming and summary task."""

from fastapi import Depends, Query, Request
from fastapi.routing import APIRouter
from fastapi_limiter.depends import RateLimiter
from fastapi_utils.cbv import cbv

from app.core.responses import AppJSONResponse, AppStreamingResponse

from .models import ChatRequest, SummaryRequest, WebSearchChatRequest
from .service import ChatService

router = APIRouter()


def common_dependency():
    """Common dependency."""
    return {"msg": "This is a dependency"}


@cbv(router)
class ChatRoute:
    """Chat-related routes."""

    def __init__(self, common_dep=Depends(common_dependency)):
        self.common_dep = common_dep
        self.service = ChatService()

    @router.get(
        "/chat",
        response_class=AppStreamingResponse,
        dependencies=[Depends(RateLimiter(times=5, seconds=60))],
    )
    async def chat(
        self,
        request: Request,
        sleep: float = Query(
            1, description="Sleep duration (in seconds) between streamed tokens."
        ),
        number: int = Query(10, description="Total number of tokens to stream."),
    ):
        """Stream chat tokens based on query parameters."""
        chat_request = ChatRequest(sleep=sleep, number=number)
        data = await self.service.chat_service(request_params=chat_request)

        return AppStreamingResponse(data_stream=data)

    @router.get(
        "/chat/websearch",
        response_class=AppStreamingResponse,
        dependencies=[Depends(RateLimiter(times=5, seconds=60))],
    )
    async def chat_websearch(
        self,
        request: Request,
        question: str = Query(
            description="The user's input question to be processed for web search and answer generation."
        ),
        thread_id: str = Query(
            description="Unique identifier for the chat thread to maintain context across requests."
        ),
    ):
        """Stream chat tokens based on query parameters."""
        chat_request = WebSearchChatRequest(question=question, thread_id=thread_id)
        data = await self.service.chat_websearch_service(request_params=chat_request)

        return AppStreamingResponse(data_stream=data)

    @router.post("/celery/summary")
    async def celery_summary(self, request: Request, request_params: SummaryRequest):
        """Submit text for summary task."""
        data, message, status_code = await self.service.submit_summary_task(
            text=request_params.text
        )

        return AppJSONResponse(data=data, message=message, status_code=status_code)

    @router.get("/celery/summary/status")
    async def celery_summary_status(
        self,
        request: Request,
        task_id: str = Query(..., description="Celery task ID to check status"),
    ):
        """Get status and result of a Celery summary task."""
        data, message, status_code = await self.service.summary_status(task_id=task_id)

        return AppJSONResponse(data=data, message=message, status_code=status_code)
