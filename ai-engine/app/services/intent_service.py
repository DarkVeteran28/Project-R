from typing import Tuple


INTENTS = [
    "availability",
    "booking",
    "hotel_information",
    "policy",
    "amenities",
    "greeting",
    "unknown",
]


def classify_intent(message: str) -> Tuple[str, float]:
    text = message.lower().strip()

    if any(word in text for word in [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good evening",
    ]):
        return "greeting", 0.99

    if any(word in text for word in [
        "available",
        "availability",
        "room tomorrow",
        "room tonight",
        "vacancy",
    ]):
        return "availability", 0.90

    if any(word in text for word in [
        "book",
        "booking",
        "reserve",
        "reservation",
    ]):
        return "booking", 0.90

    if any(word in text for word in [
        "cancel",
        "cancellation",
        "refund",
    ]):
        return "policy", 0.85

    if any(word in text for word in [
        "pool",
        "wifi",
        "gym",
        "restaurant",
        "amenities",
    ]):
        return "amenities", 0.90

    if any(word in text for word in [
        "check in",
        "check-in",
        "check out",
        "check-out",
        "location",
        "address",
        "phone number",
    ]):
        return "hotel_information", 0.85

    return "unknown", 0.40