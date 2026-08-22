from app.schemas.chat import ChatRequest, ChatResponse, Slots
from app.services.slot_service import extract_information


def process_message(request: ChatRequest) -> ChatResponse:
    extraction = extract_information(request.message)

    intent = extraction.intent
    slots = extraction.slots

    replies = {
        "greeting": "Hello! Welcome to Project R. How can I help you?",
        "availability": "Sure! I can help you check room availability.",
        "booking": "Sure! I can help you make a booking.",
        "hotel_information": "I can help you with hotel information.",
        "policy": "I can help you with the hotel's policies.",
        "amenities": "I can help you find information about the hotel's amenities.",
        "unknown": "I'm not sure I understood that. Could you please rephrase your question.",
    }

    confidence = 0.90 if intent != "unknown" else 0.40

    return ChatResponse(
        reply=replies.get(intent, replies["unknown"]),
        intent=intent,
        confidence=confidence,
        handoff_required=confidence < 0.5,
        slots=Slots(
            check_in=slots.check_in,
            check_out=slots.check_out,
            guests=slots.guests,
            room_type_id=slots.room_type_id,
            guest_name=slots.guest_name,
            phone=slots.phone,
            email=slots.email,
        ),
        action=None,
    )