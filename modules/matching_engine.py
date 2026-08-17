class MatchingEngine:
    """
    Compare resume skills with skills required by a job.
    """

    def normalize_skill(self, skill):
        """
        Normalize a skill name for comparison.
        """

        return (
            skill
            .strip()
            .lower()
            .replace("-", " ")
        )

    def extract_skill_names(self, skills):
        """
        Convert skill dictionaries into a simple list
        of normalized skill names.
        """

        skill_names = []

        for item in skills:

            if isinstance(item, dict):
                skill = item.get("skill")

            else:
                skill = item

            if skill:
                skill_names.append(
                    self.normalize_skill(skill)
                )

        return skill_names

    def match_skills(self, resume_skills, required_skills):
        """
        Compare resume skills with job-required skills.
        """

        resume_skill_names = self.extract_skill_names(
            resume_skills
        )

        required_skill_names = self.extract_skill_names(
            required_skills
        )

        # Remove duplicates
        resume_skill_names = list(
            dict.fromkeys(resume_skill_names)
        )

        required_skill_names = list(
            dict.fromkeys(required_skill_names)
        )

        matched_skills = []

        missing_skills = []

        # Find matched and missing skills
        for skill in required_skill_names:

            if skill in resume_skill_names:

                matched_skills.append(skill)

            else:

                missing_skills.append(skill)

        # Calculate percentage
        total_required = len(required_skill_names)

        if total_required == 0:

            match_percentage = 0.0

        else:

            match_percentage = (
                len(matched_skills)
                / total_required
            ) * 100

        return {
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "total_required_skills": total_required,
            "total_matched_skills": len(matched_skills),
            "skill_match_percentage": round(
                match_percentage,
                2
            )
        }