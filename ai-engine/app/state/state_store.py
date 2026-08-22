from app.state.conversation_state import ConversationState


class ConversationStateStore:
    def __init__(self):
        self._states: dict[str, ConversationState] = {}

    def get_or_create(self, conversation_id: str) -> ConversationState:
        if conversation_id not in self._states:
            self._states[conversation_id] = ConversationState()

        return self._states[conversation_id]

    def clear(self, conversation_id: str):
        self._states.pop(conversation_id, None)


state_store = ConversationStateStore()