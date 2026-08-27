from typing import Optional

from pydantic import BaseModel
from typing import Literal


IntentType = Literal[
    "greeting",
    "availability",
    "booking",
    "hotel_information",
    "policy",
    "amenities",
    "document_question",
    "unknown",
]


class ExtractedSlots(BaseModel):
    check_in: Optional[str] = None
    check_out: Optional[str] = None
    guests: Optional[int] = None
    room_type_id: Optional[str] = None
    guest_name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None


class AIExtraction(BaseModel):
    intent: IntentType
    slots: ExtractedSlots