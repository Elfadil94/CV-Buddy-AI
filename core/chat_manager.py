from core.ai_engine import ask_ai
from core.profile_manager import update_profile


def process_user_message(user_input: str, history: list) -> dict:
    """
    Process a user message.

    Returns:
        {
            "reply": "...",
            "profile": {...}
        }
    """

    result = ask_ai(user_input, history)

    profile_data = result.get("profile", {})

    update_profile(profile_data)

    return {
        "reply": result.get(
            "reply",
            "Sorry, something went wrong."
        ),
        "profile": profile_data,
    }