from typing import Optional

from pydantic import BaseModel


class ExtractedSlots(BaseModel):
    check_in: Optional[str] = None
    check_out: Optional[str] = None
    guests: Optional[int] = None
    room_type_id: Optional[str] = None
    guest_name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None


class AIExtraction(BaseModel):
    intent: str
    slots: ExtractedSlots