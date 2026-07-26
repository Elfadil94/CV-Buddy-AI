from core.profile_manager import get_profile

# ---------------------------------
# Ordered Resume Fields
# ---------------------------------

INTERVIEW_STEPS = [
    ("name", "What is your full name?"),
    ("email", "What is your email address?"),
    ("phone", "What is your phone number?"),
    ("location", "Where are you currently located?"),
    ("summary", "Can you briefly introduce yourself professionally?"),
    ("experience", "Tell me about your most recent job."),
    ("education", "Tell me about your education."),
    ("skills", "What are your main technical and professional skills?"),
    ("projects", "Have you worked on any important projects?"),
    ("languages", "Which languages do you speak?"),
]


# ---------------------------------
# Completion Percentage
# ---------------------------------

def completion_percentage() -> int:

    profile = get_profile()

    completed = 0

    if profile.name:
        completed += 1

    if profile.email:
        completed += 1

    if profile.phone:
        completed += 1

    if profile.location:
        completed += 1

    if profile.summary:
        completed += 1

    if profile.experience:
        completed += 1

    if profile.education:
        completed += 1

    if profile.skills:
        completed += 1

    if profile.projects:
        completed += 1

    if profile.languages:
        completed += 1

    return int((completed / len(INTERVIEW_STEPS)) * 100)


# ---------------------------------
# Missing Fields
# ---------------------------------

def get_missing_fields():

    profile = get_profile()

    missing = []

    if not profile.name:
        missing.append("name")

    if not profile.email:
        missing.append("email")

    if not profile.phone:
        missing.append("phone")

    if not profile.location:
        missing.append("location")

    if not profile.summary:
        missing.append("summary")

    if not profile.experience:
        missing.append("experience")

    if not profile.education:
        missing.append("education")

    if not profile.skills:
        missing.append("skills")

    if not profile.projects:
        missing.append("projects")

    if not profile.languages:
        missing.append("languages")

    return missing


# ---------------------------------
# Current Interview Step
# ---------------------------------

def current_step():

    missing = get_missing_fields()

    if not missing:
        return None

    return missing[0]


# ---------------------------------
# Next Question
# ---------------------------------

def next_question():

    step = current_step()

    if step is None:
        return None

    for field, question in INTERVIEW_STEPS:

        if field == step:
            return question

    return None


# ---------------------------------
# Interview Finished
# ---------------------------------

def interview_completed():

    return completion_percentage() == 100