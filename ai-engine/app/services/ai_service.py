from app.schemas.chat import ChatRequest, ChatResponse


def process_message(request: ChatRequest) -> ChatResponse:
    return ChatResponse(
        reply="Hello! Welcome to Hotelary. How can I help you?",
        intent="greeting",
        confidence=0.99,
        handoff_required=False,
        action=None
    )