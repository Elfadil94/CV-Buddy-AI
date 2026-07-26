from dataclasses import asdict

from core.models import (
    ResumeProfile,
    Experience,
    Education,
)

from core.storage import (
    save_json,
    load_json,
    PROFILE_FILE,
)

# ---------------------------------
# Load Profile
# ---------------------------------


def _load_profile():

    data = load_json(PROFILE_FILE)

    if not data:
        return ResumeProfile()

    profile = ResumeProfile()

    profile.name = data.get("name", "")
    profile.email = data.get("email", "")
    profile.phone = data.get("phone", "")
    profile.location = data.get("location", "")
    profile.summary = data.get("summary", "")

    profile.skills = data.get("skills", [])
    profile.projects = data.get("projects", [])
    profile.languages = data.get("languages", [])

    profile.experience = [
        Experience(**item)
        for item in data.get("experience", [])
    ]

    profile.education = [
        Education(**item)
        for item in data.get("education", [])
    ]

    return profile


_profile = _load_profile()

# ---------------------------------
# Public API
# ---------------------------------


def get_profile() -> ResumeProfile:
    return _profile


def save_profile():
    save_json(
        PROFILE_FILE,
        asdict(_profile),
    )


def reset_profile():

    global _profile

    _profile = ResumeProfile()

    save_profile()


def update_profile(data: dict):

    if not data:
        return

    if data.get("name"):
        _profile.name = data["name"]

    if data.get("email"):
        _profile.email = data["email"]

    if data.get("phone"):
        _profile.phone = data["phone"]

    if data.get("location"):
        _profile.location = data["location"]

    if data.get("summary"):
        _profile.summary = data["summary"]

    if data.get("skills"):

        for skill in data["skills"]:

            if skill not in _profile.skills:
                _profile.skills.append(skill)

    if data.get("languages"):

        for language in data["languages"]:

            if language not in _profile.languages:
                _profile.languages.append(language)

    if data.get("projects"):

        for project in data["projects"]:

            if project not in _profile.projects:
                _profile.projects.append(project)

    if data.get("experience"):

        for exp in data["experience"]:

            _profile.experience.append(
                Experience(**exp)
            )

    if data.get("education"):

        for edu in data["education"]:

            _profile.education.append(
                Education(**edu)
            )

    save_profile()