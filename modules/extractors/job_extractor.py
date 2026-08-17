import pandas as pd
from pathlib import Path
import re


class JobExtractor:
    """
    Extract structured information from a job description.
    """

    def __init__(self, skills_file):
        """
        Initialize the JobExtractor.

        Parameters
        ----------
        skills_file : str or Path
            Path to the skills database.
        """

        self.skills_file = Path(skills_file)
        self.skills_df = self.load_skills()

    def load_skills(self):
        """
        Load the skills database.
        """

        if not self.skills_file.exists():
            raise FileNotFoundError(
                f"Skills database not found: {self.skills_file}"
            )

        return pd.read_csv(self.skills_file)

    def extract_job_title(self, text):
        """
        Extract the job title from the job description.
        """

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        if not lines:
            return None

        # For Version 1, assume the first meaningful line
        # is the job title.
        return lines[0]

    def extract_skills(self, text):
        """
        Extract skills mentioned in the job description.
        """

        text_lower = text.lower()

        matched_skills = []

        for _, row in self.skills_df.iterrows():

            skill = str(row["skill"]).strip()
            category = str(row["category"]).strip()

            pattern = rf"(?<!\w){re.escape(skill.lower())}(?!\w)"

            if re.search(pattern, text_lower):

                matched_skills.append({
                    "skill": skill,
                    "category": category
                })

        return matched_skills

    def extract_experience(self, text):
        """
        Extract experience requirements from the job description.
        """

        patterns = [
            r"\b\d+\+?\s*(?:years?|yrs?)\s+(?:of\s+)?experience\b",
            r"\b\d+\s*-\s*\d+\s*(?:years?|yrs?)\s+(?:of\s+)?experience\b"
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                text,
                flags=re.IGNORECASE
            )

            if match:
                return match.group().strip()

        return None

    def extract_job_description(self, text):
        """
        Return the original job description.
        """

        return text.strip()

    def extract_job(self, text):
        """
        Extract all available job information.
        """

        return {
            "job_title": self.extract_job_title(text),

            "required_skills": self.extract_skills(text),

            "experience_required": self.extract_experience(text),

            "description": self.extract_job_description(text)
        }