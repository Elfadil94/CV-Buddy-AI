import streamlit as st

from core.chat_manager import process_user_message
from core.profile_manager import get_profile
from core.interview_engine import (
    completion_percentage,
    get_missing_fields,
)
from core.resume_generator import generate_resume_text
from core.pdf_generator import generate_resume_pdf
from core.resume_preview import render_resume_preview
from core.ats_engine import analyze_resume
from core.storage import (
    save_json,
    load_json,
    CHAT_FILE,
)

# ---------------------------------
# Page Configuration
# ---------------------------------

st.set_page_config(
    page_title="CV Buddy AI",
    page_icon="🤖",
    layout="wide",
)

profile = get_profile()

# ---------------------------------
# Header
# ---------------------------------

st.title("🤖 CV Buddy AI")
st.caption("Your AI Career Coach")

# ---------------------------------
# Sidebar
# ---------------------------------

with st.sidebar:

    st.header("📄 Resume Dashboard")

    # ATS Score

    ats = analyze_resume()

    st.subheader("📊 ATS Score")

    st.progress(ats["score"] / 100)

    st.write(f"### {ats['score']} / 100")

    if ats["strengths"]:

        st.success("Strengths")

        for item in ats["strengths"]:
            st.write(f"✅ {item}")

    if ats["improvements"]:

        st.warning("Improvements")

        for item in ats["improvements"]:
            st.write(f"⚠️ {item}")

    st.divider()

    # Resume Completion

    progress = completion_percentage()

    st.subheader("📈 Resume Completion")

    st.progress(progress / 100)

    st.write(f"### {progress}% Complete")

    missing = get_missing_fields()

    if missing:

        st.warning("Missing Information")

        for field in missing:
            st.write(f"• {field.replace('_', ' ').title()}")

    else:

        st.success("🎉 Resume Completed!")

    st.divider()

    # Basic Information

    st.subheader("👤 Basic Information")

    st.write("**Name:**", profile.name or "-")
    st.write("**Email:**", profile.email or "-")
    st.write("**Phone:**", profile.phone or "-")
    st.write("**Location:**", profile.location or "-")

    st.divider()

    # Downloads

    st.subheader("⬇️ Downloads")

    resume_text = generate_resume_text()

    st.download_button(
        "📄 Download TXT",
        resume_text,
        "resume.txt",
        "text/plain",
        use_container_width=True,
    )

    pdf_bytes = generate_resume_pdf(profile)

    st.download_button(
        "📕 Download PDF",
        pdf_bytes,
        "resume.pdf",
        "application/pdf",
        use_container_width=True,
    )

# ---------------------------------
# Session State
# ---------------------------------

if "messages" not in st.session_state:

    saved_messages = load_json(CHAT_FILE)

    if saved_messages:

        st.session_state.messages = saved_messages

    else:

        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "Hello 👋\n\n"
                    "I'm CV Buddy AI.\n\n"
                    "I'll help you build a professional resume.\n\n"
                    "Let's start.\n\n"
                    "What is your name?"
                ),
            }
        ]

# ---------------------------------
# Layout
# ---------------------------------

chat_col, resume_col = st.columns([1.1, 0.9])

# =================================
# CHAT
# =================================

with chat_col:

    st.subheader("💬 Career Interview")

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    user_input = st.chat_input("Type your answer...")

    if user_input:

        # User Message

        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_input,
            }
        )

        save_json(
            CHAT_FILE,
            st.session_state.messages,
        )

        # Build History

        history = []

        for msg in st.session_state.messages:

            history.append(
                {
                    "role": msg["role"],
                    "text": msg["content"],
                }
            )

        # AI Response

        result = process_user_message(
            user_input=user_input,
            history=history,
        )

        reply = result.get(
            "reply",
            "Sorry, something went wrong.",
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": reply,
            }
        )

        save_json(
            CHAT_FILE,
            st.session_state.messages,
        )

        st.rerun()

# =================================
# LIVE RESUME
# =================================

with resume_col:

    render_resume_preview()