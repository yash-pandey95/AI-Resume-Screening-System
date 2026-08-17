import re


class ATSEngine:
    """
    Calculate an ATS score by comparing a resume
    against a job description.
    """

    def __init__(
        self,
        skill_weight=60,
        education_weight=15,
        experience_weight=15,
        keyword_weight=10
    ):
        """
        Initialize ATS scoring weights.

        Total weight must equal 100.
        """

        total_weight = (
            skill_weight
            + education_weight
            + experience_weight
            + keyword_weight
        )

        if total_weight != 100:
            raise ValueError(
                "ATS weights must add up to 100."
            )

        self.skill_weight = skill_weight
        self.education_weight = education_weight
        self.experience_weight = experience_weight
        self.keyword_weight = keyword_weight

    # --------------------------------------------------
    # Education Match
    # --------------------------------------------------

    def calculate_education_match(self, resume, job):
        """
        Calculate education match.

        Version 1:
        If the job description contains a degree requirement,
        compare it with the resume education.

        If no degree requirement is found,
        give full education score.
        """

        education = resume.get("education", {})

        degrees = education.get("degrees", [])

        description = job.get(
            "description",
            ""
        ).lower()

        if not degrees:
            return 0.0

        # Degree keywords commonly found in job descriptions
        degree_keywords = [
            "b.tech",
            "btech",
            "b tech",
            "b.e",
            "be",
            "bachelor",
            "m.tech",
            "mtech",
            "m tech",
            "m.e",
            "me",
            "master",
            "phd",
            "doctorate"
        ]

        required_degree = None

        for keyword in degree_keywords:

            if keyword in description:
                required_degree = keyword
                break

        # No education requirement mentioned
        if required_degree is None:
            return 100.0

        # Check resume degrees
        for degree in degrees:

            resume_degree = degree.get(
                "degree",
                ""
            ).lower()

            category = degree.get(
                "category",
                ""
            ).lower()

            if (
                required_degree in resume_degree
                or required_degree in category
                or "bachelor" in required_degree
                and "bachelor" in category
                or "master" in required_degree
                and "master" in category
            ):
                return 100.0

        return 0.0

    # --------------------------------------------------
    # Experience Match
    # --------------------------------------------------

    def calculate_experience_match(
        self,
        resume,
        job
    ):
        """
        Calculate experience match.

        Version 1:
        Compare required years with resume experience.
        """

        required = job.get(
            "experience_required"
        )

        experiences = resume.get(
            "experience",
            {}
        )

        experience_list = experiences.get(
            "experiences",
            []
        )

        # If job doesn't specify experience,
        # don't penalize the candidate.
        if not required:
            return 100.0

        # Extract required years
        required_match = re.search(
            r"\d+",
            required
        )

        if not required_match:
            return 100.0

        required_years = int(
            required_match.group()
        )

        # No experience found
        if not experience_list:
            return 0.0

        # Version 1:
        # Count years mentioned in experience entries.
        experience_years = set()

        for experience in experience_list:

            years = experience.get(
                "years",
                []
            )

            for year in years:
                experience_years.add(year)

        # Rough estimate
        # This will be improved later.
        if len(experience_years) >= required_years + 1:
            return 100.0

        if len(experience_years) >= required_years:
            return 100.0

        return 50.0

    # --------------------------------------------------
    # Keyword Match
    # --------------------------------------------------

    def calculate_keyword_match(
        self,
        resume,
        job
    ):
        """
        Compare important job keywords against
        the resume text.
        """

        resume_text = resume.get(
            "resume_text",
            ""
        ).lower()

        job_description = job.get(
            "description",
            ""
        ).lower()

        # Extract words with at least 4 characters
        job_words = re.findall(
            r"\b[a-zA-Z]{4,}\b",
            job_description
        )

        resume_words = set(
            re.findall(
                r"\b[a-zA-Z]{4,}\b",
                resume_text
            )
        )

        # Remove common words
        stop_words = {
            "with",
            "from",
            "this",
            "that",
            "have",
            "will",
            "your",
            "their",
            "they",
            "about",
            "into",
            "should",
            "looking",
            "candidate",
            "experience"
        }

        job_words = [
            word
            for word in job_words
            if word not in stop_words
        ]

        job_words = list(
            dict.fromkeys(job_words)
        )

        if not job_words:
            return 0.0

        matched_words = [
            word
            for word in job_words
            if word in resume_words
        ]

        percentage = (
            len(matched_words)
            / len(job_words)
        ) * 100

        return round(
            min(percentage, 100),
            2
        )

    # --------------------------------------------------
    # Overall ATS Score
    # --------------------------------------------------

    def calculate_score(
        self,
        resume,
        job,
        matching_result
    ):
        """
        Calculate final ATS score.
        """

        # Skill score
        skill_match = matching_result.get(
            "skill_match_percentage",
            0.0
        )

        # Education score
        education_match = (
            self.calculate_education_match(
                resume,
                job
            )
        )

        # Experience score
        experience_match = (
            self.calculate_experience_match(
                resume,
                job
            )
        )

        # Keyword score
        keyword_match = (
            self.calculate_keyword_match(
                resume,
                job
            )
        )

        # Weighted score
        overall_score = (
            skill_match * self.skill_weight / 100
            +
            education_match * self.education_weight / 100
            +
            experience_match * self.experience_weight / 100
            +
            keyword_match * self.keyword_weight / 100
        )

        return {
            "overall_score": round(
                overall_score,
                2
            ),

            "skill_match": round(
                skill_match,
                2
            ),

            "education_match": round(
                education_match,
                2
            ),

            "experience_match": round(
                experience_match,
                2
            ),

            "keyword_match": round(
                keyword_match,
                2
            ),

            "weights": {
                "skills": self.skill_weight,
                "education": self.education_weight,
                "experience": self.experience_weight,
                "keywords": self.keyword_weight
            }
        }