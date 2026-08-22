REQUIRED_SLOTS = {
    "booking": [
        "check_in",
        "check_out",
        "guests",
        "room_type_id",
        "guest_name",
        "phone",
    ],
    "availability": [
        "check_in",
        "check_out",
        "guests",
    ],
}


def get_missing_slots(intent: str, slots: dict) -> list[str]:
    required = REQUIRED_SLOTS.get(intent, [])

    return [
        slot
        for slot in required
        if slots.get(slot) is None
    ]