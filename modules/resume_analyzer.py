class ResumeAnalyzer:
    """
    Analyze a resume against a job and generate
    strengths, weaknesses, and improvement suggestions.
    """

    def __init__(self):
        pass

    # --------------------------------------------------
    # Strength Analysis
    # --------------------------------------------------

    def analyze_strengths(
        self,
        resume,
        matching_result,
        ats_result
    ):
        """
        Identify strong areas of the resume.
        """

        strengths = []

        # Strong skill match
        skill_match = matching_result.get(
            "skill_match_percentage",
            0
        )

        if skill_match >= 80:

            strengths.append(
                f"Strong technical skill match "
                f"({skill_match}%) with the job."
            )

        elif skill_match >= 60:

            strengths.append(
                f"Good technical skill match "
                f"({skill_match}%) with the job."
            )

        # Education
        education_match = ats_result.get(
            "education_match",
            0
        )

        if education_match >= 80:

            strengths.append(
                "Education requirements are well aligned "
                "with the job."
            )

        # Experience
        experience_match = ats_result.get(
            "experience_match",
            0
        )

        if experience_match >= 80:

            strengths.append(
                "Work experience appears relevant "
                "to the position."
            )

        # Number of skills
        skills = resume.get(
            "skills",
            []
        )

        if len(skills) >= 10:

            strengths.append(
                "Resume demonstrates a broad technical "
                "skill set."
            )

        # Projects
        projects = resume.get(
            "projects",
            []
        )

        if projects:

            strengths.append(
                "Resume includes project experience."
            )

        # If nothing found
        if not strengths:

            strengths.append(
                "Resume contains some relevant "
                "information for the target role."
            )

        return strengths

    # --------------------------------------------------
    # Weakness Analysis
    # --------------------------------------------------

    def analyze_weaknesses(
        self,
        resume,
        matching_result,
        ats_result
    ):
        """
        Identify weak areas in the resume.
        """

        weaknesses = []

        skill_match = matching_result.get(
            "skill_match_percentage",
            0
        )

        missing_skills = matching_result.get(
            "missing_skills",
            []
        )

        experience_match = ats_result.get(
            "experience_match",
            0
        )

        keyword_match = ats_result.get(
            "keyword_match",
            0
        )

        # Skill weakness
        if skill_match < 60:

            weaknesses.append(
                f"Low technical skill match "
                f"({skill_match}%) for this job."
            )

        elif skill_match < 80:

            weaknesses.append(
                f"Some important job skills are missing "
                f"({skill_match}% skill match)."
            )

        # Missing skills
        if missing_skills:

            weaknesses.append(
                "The resume is missing "
                f"{len(missing_skills)} required or "
                "relevant skills."
            )

        # Experience
        if experience_match < 80:

            weaknesses.append(
                "The resume does not strongly demonstrate "
                "the required level of experience."
            )

        # Keywords
        if keyword_match < 60:

            weaknesses.append(
                "The resume contains relatively few "
                "keywords relevant to the job description."
            )

        # Education
        education_match = ats_result.get(
            "education_match",
            0
        )

        if education_match < 80:

            weaknesses.append(
                "Education requirements may not fully "
                "match the target position."
            )

        # No projects
        projects = resume.get(
            "projects",
            []
        )

        if not projects:

            weaknesses.append(
                "No structured project information "
                "was detected."
            )

        return weaknesses

    # --------------------------------------------------
    # Recommendations
    # --------------------------------------------------

    def generate_recommendations(
        self,
        resume,
        matching_result,
        ats_result
    ):
        """
        Generate actionable recommendations.
        """

        recommendations = []

        missing_skills = matching_result.get(
            "missing_skills",
            []
        )

        skill_match = matching_result.get(
            "skill_match_percentage",
            0
        )

        keyword_match = ats_result.get(
            "keyword_match",
            0
        )

        experience_match = ats_result.get(
            "experience_match",
            0
        )

        # Missing skills
        if missing_skills:

            skills_text = ", ".join(
                missing_skills
            )

            recommendations.append(
                "Consider learning or demonstrating "
                f"these missing skills: {skills_text}."
            )

        # Skill match
        if skill_match < 80:

            recommendations.append(
                "Add relevant technical skills only when "
                "you genuinely have experience with them."
            )

        # Keywords
        if keyword_match < 70:

            recommendations.append(
                "Use relevant terminology from the job "
                "description naturally in your resume."
            )

        # Experience
        if experience_match < 80:

            recommendations.append(
                "Add measurable achievements and concrete "
                "results to your experience or projects."
            )

        # Projects
        projects = resume.get(
            "projects",
            []
        )

        if not projects:

            recommendations.append(
                "Add 2-3 relevant projects with technologies "
                "used and measurable outcomes."
            )

        # General recommendation
        recommendations.append(
            "Keep the resume concise, structured, and "
            "focused on the target role."
        )

        return recommendations

    # --------------------------------------------------
    # Overall Analysis
    # --------------------------------------------------

    def generate_summary(
        self,
        ats_result,
        matching_result
    ):
        """
        Generate a simple overall resume assessment.
        """

        score = ats_result.get(
            "overall_score",
            0
        )

        if score >= 85:

            level = "Excellent"

        elif score >= 70:

            level = "Good"

        elif score >= 50:

            level = "Needs Improvement"

        else:

            level = "Weak"

        return (
            f"{level} match for the target job "
            f"with an ATS score of {score}/100."
        )

    # --------------------------------------------------
    # Complete Analysis
    # --------------------------------------------------

    def analyze(
        self,
        resume,
        job,
        matching_result,
        ats_result
    ):
        """
        Generate complete resume analysis.
        """

        strengths = self.analyze_strengths(
            resume,
            matching_result,
            ats_result
        )

        weaknesses = self.analyze_weaknesses(
            resume,
            matching_result,
            ats_result
        )

        recommendations = self.generate_recommendations(
            resume,
            matching_result,
            ats_result
        )

        summary = self.generate_summary(
            ats_result,
            matching_result
        )

        return {
            "summary": summary,
            "strengths": strengths,
            "weaknesses": weaknesses,
            "missing_skills": matching_result.get(
                "missing_skills",
                []
            ),
            "recommendations": recommendations
        }