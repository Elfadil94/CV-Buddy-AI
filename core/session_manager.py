import streamlit as st

# ---------------------------------
# Default Welcome Message
# ---------------------------------

WELCOME_MESSAGE = {
    "role": "assistant",
    "content": (
        "Hello 👋\n\n"
        "I'm CV Buddy AI.\n\n"
        "I'll help you build a professional resume.\n\n"
        "Let's start.\n\n"
        "What is your name?"
    ),
}

# ---------------------------------
# Initialize Session
# ---------------------------------

def initialize_session():

    if "messages" not in st.session_state:

        st.session_state.messages = [
            WELCOME_MESSAGE.copy()
        ]

# ---------------------------------
# Get Messages
# ---------------------------------

def get_messages():

    initialize_session()

    return st.session_state.messages

# ---------------------------------
# Add Message
# ---------------------------------

def add_message(role: str, content: str):

    initialize_session()

    st.session_state.messages.append(
        {
            "role": role,
            "content": content,
        }
    )

# ---------------------------------
# Build AI History
# ---------------------------------

def build_history():

    initialize_session()

    history = []

    for msg in st.session_state.messages:

        history.append(
            {
                "role": msg["role"],
                "text": msg["content"],
            }
        )

    return history

# ---------------------------------
# Reset Session
# ---------------------------------

def reset_session():

    st.session_state.messages = [
        WELCOME_MESSAGE.copy()
    ]