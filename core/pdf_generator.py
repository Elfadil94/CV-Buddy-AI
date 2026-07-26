from io import BytesIO

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
)

from core.models import ResumeProfile


def generate_resume_pdf(profile: ResumeProfile) -> bytes:

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    # ---------------------------------
    # Name
    # ---------------------------------

    story.append(
        Paragraph(
            f"<font size=20><b>{profile.name}</b></font>",
            styles["Title"],
        )
    )

    story.append(Spacer(1, 12))

    # ---------------------------------
    # Contact
    # ---------------------------------

    contact = []

    if profile.email:
        contact.append(profile.email)

    if profile.phone:
        contact.append(profile.phone)

    if profile.location:
        contact.append(profile.location)

    if contact:

        story.append(
            Paragraph(
                " | ".join(contact),
                styles["Normal"],
            )
        )

        story.append(Spacer(1, 18))

    # ---------------------------------
    # Summary
    # ---------------------------------

    if profile.summary:

        story.append(
            Paragraph(
                "<b>Professional Summary</b>",
                styles["Heading2"],
            )
        )

        story.append(
            Paragraph(
                profile.summary,
                styles["BodyText"],
            )
        )

        story.append(Spacer(1, 12))

    # ---------------------------------
    # Skills
    # ---------------------------------

    if profile.skills:

        story.append(
            Paragraph(
                "<b>Skills</b>",
                styles["Heading2"],
            )
        )

        for skill in profile.skills:

            story.append(
                Paragraph(
                    f"• {skill}",
                    styles["BodyText"],
                )
            )

        story.append(Spacer(1, 12))

    # ---------------------------------
    # Experience
    # ---------------------------------

    if profile.experience:

        story.append(
            Paragraph(
                "<b>Experience</b>",
                styles["Heading2"],
            )
        )

        for exp in profile.experience:

            title = f"{exp.position} - {exp.company}"

            story.append(
                Paragraph(
                    title,
                    styles["Heading3"],
                )
            )

            dates = f"{exp.start_date} - {exp.end_date}"

            story.append(
                Paragraph(
                    dates,
                    styles["Italic"],
                )
            )

            if exp.description:

                story.append(
                    Paragraph(
                        exp.description,
                        styles["BodyText"],
                    )
                )

            story.append(Spacer(1, 10))

    # ---------------------------------
    # Education
    # ---------------------------------

    if profile.education:

        story.append(
            Paragraph(
                "<b>Education</b>",
                styles["Heading2"],
            )
        )

        for edu in profile.education:

            story.append(
                Paragraph(
                    f"{edu.degree}",
                    styles["Heading3"],
                )
            )

            story.append(
                Paragraph(
                    f"{edu.school} ({edu.graduation_year})",
                    styles["BodyText"],
                )
            )

            story.append(Spacer(1, 10))

    # ---------------------------------
    # Projects
    # ---------------------------------

    if profile.projects:

        story.append(
            Paragraph(
                "<b>Projects</b>",
                styles["Heading2"],
            )
        )

        for project in profile.projects:

            story.append(
                Paragraph(
                    f"• {project}",
                    styles["BodyText"],
                )
            )

        story.append(Spacer(1, 12))

    # ---------------------------------
    # Languages
    # ---------------------------------

    if profile.languages:

        story.append(
            Paragraph(
                "<b>Languages</b>",
                styles["Heading2"],
            )
        )

        for language in profile.languages:

            story.append(
                Paragraph(
                    f"• {language}",
                    styles["BodyText"],
                )
            )

    doc.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf