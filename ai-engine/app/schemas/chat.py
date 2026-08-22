from typing import Optional

from pydantic import BaseModel


class ChatRequest(BaseModel):
    hotel_id: str
    conversation_id: str
    message: str


class Slots(BaseModel):
    check_in: Optional[str] = None
    check_out: Optional[str] = None
    guests: Optional[int] = None
    room_type_id: Optional[str] = None
    guest_name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None


class Action(BaseModel):
    type: str
    status: str
    booking_id: Optional[str] = None


class ChatResponse(BaseModel):
    reply: str
    intent: str
    confidence: float
    handoff_required: bool
    slots: Slots
    action: Optional[Action] = None