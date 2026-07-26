from core.profile_manager import get_profile


def analyze_resume():
    """
    Analyze the current resume profile and return an ATS score.
    """

    profile = get_profile()

    score = 0

    strengths = []
    improvements = []

    # -----------------------------
    # Contact Information
    # -----------------------------

    if profile.name:
        score += 10
    else:
        improvements.append("Add your full name")

    if profile.email:
        score += 10
    else:
        improvements.append("Add your email")

    if profile.phone:
        score += 10
    else:
        improvements.append("Add your phone number")

    if profile.location:
        score += 5
    else:
        improvements.append("Add your location")

    # -----------------------------
    # Summary
    # -----------------------------

    if profile.summary:
        score += 15
        strengths.append("Professional Summary")
    else:
        improvements.append("Write a professional summary")

    # -----------------------------
    # Skills
    # -----------------------------

    if len(profile.skills) >= 5:
        score += 15
        strengths.append("Technical Skills")

    elif len(profile.skills) > 0:
        score += 8
        improvements.append("Add more technical skills")

    else:
        improvements.append("Add technical skills")

    # -----------------------------
    # Experience
    # -----------------------------

    if len(profile.experience) > 0:
        score += 15
        strengths.append("Work Experience")
    else:
        improvements.append("Add work experience")

    # -----------------------------
    # Education
    # -----------------------------

    if len(profile.education) > 0:
        score += 10
        strengths.append("Education")
    else:
        improvements.append("Add education")

    # -----------------------------
    # Projects
    # -----------------------------

    if len(profile.projects) > 0:
        score += 5
        strengths.append("Projects")
    else:
        improvements.append("Add personal or professional projects")

    # -----------------------------
    # Languages
    # -----------------------------

    if len(profile.languages) > 0:
        score += 5
        strengths.append("Languages")
    else:
        improvements.append("Add spoken languages")

    # -----------------------------
    # Limit Score
    # -----------------------------

    score = min(score, 100)

    return {
        "score": score,
        "strengths": strengths,
        "improvements": improvements,
    }