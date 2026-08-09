import pandas as pd
from pathlib import Path
import re


class EducationExtractor:
    """
    Extract education-related information from resume text.
    """

    def __init__(self, degrees_file):
        """
        Initialize the EducationExtractor.
        """

        self.degrees_file = Path(degrees_file)
        self.degrees_df = self.load_degrees()

    def load_degrees(self):
        """
        Load degree database from CSV.
        """

        if not self.degrees_file.exists():
            raise FileNotFoundError(
                f"Degree database not found: {self.degrees_file}"
            )

        return pd.read_csv(self.degrees_file)

    def extract_degrees(self, text):
        """
        Extract degrees from resume text.
        """

        text = text.lower()

        matched_degrees = []

        for _, row in self.degrees_df.iterrows():

            degree = str(row["degree"]).strip()
            category = str(row["category"]).strip()

            pattern = rf"(?<!\w){re.escape(degree.lower())}(?!\w)"

            if re.search(pattern, text):

                matched_degrees.append({
                    "degree": degree,
                    "category": category
                })

        return matched_degrees

    def extract_university(self, text):
        """
        Extract university, institute, or college name.
        """

        # Remove common resume section headings
        clean_text = re.sub(
            r"\b(EDUCATION|EXPERIENCE|PROJECTS|SKILLS|CERTIFICATIONS)\b",
            "",
            text,
            flags=re.IGNORECASE
        )

        pattern = (
            r"\b([A-Z][A-Za-z0-9&.,'()-]*"
            r"(?:\s+[A-Z][A-Za-z0-9&.,'()-]*)*)"
            r"\s+(University|Institute|College)\b"
        )

        matches = re.findall(
            pattern,
            clean_text
        )

        if matches:

            # matches[0] is a tuple:
            # ("Quantum", "University")
            #
            # Join both parts together.

            name = " ".join(matches[0]).strip()

            return name

        return None

    def extract_years(self, text):
        """
        Extract education-related years.
        """

        education_pattern = (
            r"(?:education|academic|qualification|degree)"
            r".{0,300}?"
            r"((?:19|20)\d{2})"
            r".{0,100}?"
            r"((?:19|20)\d{2})"
        )

        match = re.search(
            education_pattern,
            text,
            flags=re.IGNORECASE
        )

        if match:

            return list(match.groups())

        return []

    def extract_education(self, text):
        """
        Extract all education information from resume text.
        """

        degrees = self.extract_degrees(text)

        university = self.extract_university(text)

        years = self.extract_years(text)

        return {
            "degrees": degrees,
            "university": university,
            "years": years
        }