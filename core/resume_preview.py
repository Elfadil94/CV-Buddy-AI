import streamlit as st

from core.profile_manager import get_profile


def render_resume_preview():
    """
    Render the live resume preview.
    """

    profile = get_profile()

    st.subheader("📄 Live Resume")

    st.markdown("---")

    # ---------------------------------
    # Name
    # ---------------------------------

    st.markdown(f"# {profile.name or 'Your Name'}")

    st.write(
        " | ".join(
            filter(
                None,
                [
                    profile.email,
                    profile.phone,
                    profile.location,
                ],
            )
        )
    )

    st.markdown("---")

    # ---------------------------------
    # Summary
    # ---------------------------------

    st.markdown("## Professional Summary")

    if profile.summary:
        st.write(profile.summary)
    else:
        st.caption("Professional summary will appear here.")

    # ---------------------------------
    # Skills
    # ---------------------------------

    st.markdown("## Skills")

    if profile.skills:

        for skill in profile.skills:
            st.markdown(f"- {skill}")

    else:

        st.caption("No skills added yet.")

    # ---------------------------------
    # Experience
    # ---------------------------------

    st.markdown("## Experience")

    if profile.experience:

        for exp in profile.experience:

            st.markdown(f"### {exp.position}")
            st.write(exp.company)

            dates = " - ".join(
                filter(
                    None,
                    [
                        exp.start_date,
                        exp.end_date,
                    ],
                )
            )

            if dates:
                st.caption(dates)

            if exp.description:
                st.write(exp.description)

            st.markdown("---")

    else:

        st.caption("No experience added yet.")

    # ---------------------------------
    # Education
    # ---------------------------------

    st.markdown("## Education")

    if profile.education:

        for edu in profile.education:

            st.markdown(f"### {edu.degree}")
            st.write(edu.school)

            if edu.graduation_year:
                st.caption(edu.graduation_year)

    else:

        st.caption("No education added yet.")

    # ---------------------------------
    # Projects
    # ---------------------------------

    st.markdown("## Projects")

    if profile.projects:

        for project in profile.projects:
            st.markdown(f"- {project}")

    else:

        st.caption("No projects added yet.")

    # ---------------------------------
    # Languages
    # ---------------------------------

    st.markdown("## Languages")

    if profile.languages:

        for language in profile.languages:
            st.markdown(f"- {language}")

    else:

        st.caption("No languages added yet.")