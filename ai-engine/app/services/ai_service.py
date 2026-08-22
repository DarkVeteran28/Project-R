from app.schemas.chat import ChatRequest, ChatResponse, Slots
from app.services.intent_service import classify_intent


def process_message(request: ChatRequest) -> ChatResponse:
    intent, confidence = classify_intent(request.message)

    replies = {
        "greeting": "Hello! Welcome to Hotelary. How can I help you?",
        "availability": "Sure! I can help you check room availability.",
        "booking": "Sure! I can help you make a booking.",
        "hotel_information": "I can help you with hotel information.",
        "policy": "I can help you with the hotel's policies.",
        "amenities": "I can help you find information about the hotel's amenities.",
        "unknown": "I'm not sure I understood that. Could you please rephrase your question?",
    }

    return ChatResponse(
        reply=replies[intent],
        intent=intent,
        confidence=confidence,
        handoff_required=confidence < 0.5,
        slots=Slots(),
        action=None,
    )