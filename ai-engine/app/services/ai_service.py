from app.schemas.chat import ChatRequest, ChatResponse, Slots
from app.services.slot_service import extract_information
from app.services.slot_requirements import get_missing_slots
from app.state.state_store import state_store
from app.rag.rag_service import ask_document


def process_message(request: ChatRequest) -> ChatResponse:
    # Get or create conversation state
    state = state_store.get_or_create(
        request.conversation_id
    )

    # Extract intent and slots from the current message
    extraction = extract_information(
        request.message
    )

    # Merge newly extracted information with existing state
    state.update(
        intent=extraction.intent,
        new_slots=extraction.slots,
    )

    # Get updated conversation state
    current_state = state.get_state()

    intent = current_state["intent"]
    slots = current_state["slots"]

    # Check which required slots are still missing
    missing_slots = get_missing_slots(
        intent,
        slots,
    )

    # Default responses for intents
    replies = {
        "greeting": "Hello! Welcome to Hotelary. How can I help you?",
        "availability": "Sure! I can help you check room availability.",
        "booking": "Sure! I can help you make a booking.",
        "hotel_information": "I can help you with hotel information.",
        "policy": "I can help you with the hotel's policies.",
        "amenities": "I can help you find information about the hotel's amenities.",
        "document_question": (
            "I'll look through the provided document "
            "to find the relevant information."
        ),
        "unknown": (
            "I'm not sure I understood that. "
            "Could you please rephrase your question?"
        ),
    }

    # Route document questions to RAG
    if intent == "document_question":
        reply = ask_document(
            hotel_id=request.hotel_id,
            conversation_id=request.conversation_id,
            question=request.message,
        )

    # Handle booking when required information is missing
    elif intent == "booking" and missing_slots:
        next_slot = missing_slots[0]

        questions = {
            "check_in": "What date would you like to check in?",
            "check_out": "What date would you like to check out?",
            "guests": "How many guests will be staying?",
            "room_type_id": "What type of room would you prefer?",
            "guest_name": "What name should I use for the booking?",
            "phone": "What phone number should I use for the booking?",
        }

        reply = questions.get(
            next_slot,
            "Could you provide a little more information?",
        )

    # Handle all other intents
    else:
        reply = replies.get(
            intent,
            replies["unknown"],
        )

    # Temporary confidence logic
    confidence = 0.90 if intent != "unknown" else 0.40

    return ChatResponse(
        reply=reply,
        intent=intent,
        confidence=confidence,
        handoff_required=confidence < 0.5,
        slots=Slots(**slots),
        action=None,
    )