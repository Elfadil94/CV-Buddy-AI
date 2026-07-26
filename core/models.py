from dataclasses import dataclass, field


@dataclass
class Experience:
    company: str = ""
    position: str = ""
    start_date: str = ""
    end_date: str = ""
    description: str = ""


@dataclass
class Education:
    school: str = ""
    degree: str = ""
    graduation_year: str = ""


@dataclass
class ResumeProfile:
    name: str = ""
    email: str = ""
    phone: str = ""
    location: str = ""

    summary: str = ""

    skills: list[str] = field(default_factory=list)

    experience: list[Experience] = field(default_factory=list)

    education: list[Education] = field(default_factory=list)

    projects: list[str] = field(default_factory=list)

    languages: list[str] = field(default_factory=list)