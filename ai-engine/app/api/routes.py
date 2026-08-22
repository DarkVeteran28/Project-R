from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.ai_service import process_message


router = APIRouter()


@router.post("/ai/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return process_message(request)