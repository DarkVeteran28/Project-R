from pydantic import BaseModel
from typing import Optional


class ChatRequest(BaseModel):
    hotel_id: str
    conversation_id: str
    message: str


class Action(BaseModel):
    type: str
    status: str
    booking_id: Optional[str] = None


class ChatResponse(BaseModel):
    reply: str
    intent: str
    confidence: float
    handoff_required: bool
    action: Optional[Action] = None