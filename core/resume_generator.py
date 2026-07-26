from core.profile_manager import get_profile


def generate_resume_text():

    profile = get_profile()

    resume = []

    # -----------------------------
    # Header
    # -----------------------------

    resume.append(profile.name or "Your Name")
    resume.append("=" * 50)

    if profile.email:
        resume.append(f"Email: {profile.email}")

    if profile.phone:
        resume.append(f"Phone: {profile.phone}")

    if profile.location:
        resume.append(f"Location: {profile.location}")

    resume.append("")

    # -----------------------------
    # Professional Summary
    # -----------------------------

    if profile.summary:

        resume.append("PROFESSIONAL SUMMARY")
        resume.append("-" * 50)
        resume.append(profile.summary)
        resume.append("")

    # -----------------------------
    # Skills
    # -----------------------------

    if profile.skills:

        resume.append("SKILLS")
        resume.append("-" * 50)

        for skill in profile.skills:
            resume.append(f"• {skill}")

        resume.append("")

    # -----------------------------
    # Languages
    # -----------------------------

    if profile.languages:

        resume.append("LANGUAGES")
        resume.append("-" * 50)

        for language in profile.languages:
            resume.append(f"• {language}")

        resume.append("")

    return "\n".join(resume)