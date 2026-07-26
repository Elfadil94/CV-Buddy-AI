import json
import os
import time

from dotenv import load_dotenv
from google import genai

from core.prompts import SYSTEM_PROMPT

# ---------------------------------
# Load Environment Variables
# ---------------------------------

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY was not found in your .env file."
    )

# ---------------------------------
# Gemini Client
# ---------------------------------

client = genai.Client(api_key=API_KEY)

# ---------------------------------
# Gemini Models (Fallback Order)
# ---------------------------------

MODELS = [
    "gemini-3.5-flash",
    "gemini-3.6-flash",
    "gemini-flash-latest",
    "gemini-3.5-flash-lite",
]

# ---------------------------------
# Chat with AI
# ---------------------------------


def ask_ai(user_message: str, history: list | None = None) -> dict:
    """
    Send a message to Gemini.

    Returns:
    {
        "reply": "...",
        "profile": {...}
    }
    """

    if history is None:
        history = []

    conversation = SYSTEM_PROMPT + "\n\n"

    for item in history:

        role = item.get("role", "user")
        text = item.get("text", "")

        conversation += f"{role}: {text}\n"

    conversation += f"user: {user_message}"

    last_error = None

    # ---------------------------------
    # Try Each Model
    # ---------------------------------

    for model in MODELS:

        print(f"\nUsing model: {model}")

        for attempt in range(3):

            try:

                response = client.models.generate_content(
                    model=model,
                    contents=conversation,
                )

                text = response.text.strip()

                # Remove Markdown JSON fences if present
                text = text.replace("```json", "")
                text = text.replace("```", "")
                text = text.strip()

                # -----------------------------
                # Parse JSON
                # -----------------------------

                try:

                    data = json.loads(text)

                    return {
                        "reply": data.get("reply", ""),
                        "profile": data.get("profile", {}),
                    }

                except json.JSONDecodeError:

                    # AI returned plain text instead of JSON

                    return {
                        "reply": text,
                        "profile": {},
                    }

            except Exception as e:

                last_error = e

                print(
                    f"[{model}] Attempt {attempt + 1}/3 failed:"
                )
                print(e)

                if attempt < 2:

                    time.sleep(3)

        print(f"Switching to next model...\n")

    # ---------------------------------
    # All Models Failed
    # ---------------------------------

    print(last_error)

    return {
        "reply": (
            "⚠️ All AI models are currently busy.\n\n"
            "Please wait a minute and try again."
        ),
        "profile": {},
    }