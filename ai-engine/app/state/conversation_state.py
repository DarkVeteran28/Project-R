from app.schemas.ai_output import ExtractedSlots


class ConversationState:
    def __init__(self):
        self.intent: str | None = None
        self.slots = ExtractedSlots()

    def update(
        self,
        intent: str | None,
        new_slots: ExtractedSlots,
    ):
        if intent:
            self.intent = intent

        for field in new_slots.model_fields:
            new_value = getattr(new_slots, field)

            if new_value is not None:
                setattr(self.slots, field, new_value)

    def get_state(self):
        return {
            "intent": self.intent,
            "slots": self.slots.model_dump(),
        }