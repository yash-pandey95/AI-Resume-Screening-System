import re


class ExperienceExtractor:
    """
    Extract work experience information from resume text.
    """

    EXPERIENCE_HEADINGS = [
        "experience",
        "work experience",
        "professional experience",
        "employment",
        "work history",
        "employment history",
        "internship",
        "internships"
    ]

    NEXT_SECTION_HEADINGS = [
        "education",
        "skills",
        "technical skills",
        "projects",
        "certifications",
        "certificates",
        "achievements",
        "awards",
        "languages",
        "summary",
        "objective",
        "interests"
    ]

    ROLE_KEYWORDS = [
        "intern",
        "engineer",
        "developer",
        "analyst",
        "scientist",
        "manager",
        "designer",
        "consultant",
        "administrator",
        "architect",
        "specialist",
        "associate",
        "lead",
        "executive",
        "trainee",
        "researcher"
    ]

    def __init__(self):
        pass

    def extract_experience_section(self, text):
        """
        Extract the section of the resume that contains
        work experience.
        """

        lines = text.splitlines()

        start_index = None
        end_index = len(lines)

        # Find the experience heading
        for i, line in enumerate(lines):

            clean_line = line.strip().lower()

            if clean_line in self.EXPERIENCE_HEADINGS:
                start_index = i + 1
                break

        # If no experience section is found
        if start_index is None:
            return ""

        # Find where the experience section ends
        for i in range(start_index, len(lines)):

            clean_line = lines[i].strip().lower()

            if clean_line in self.NEXT_SECTION_HEADINGS:
                end_index = i
                break

        experience_lines = lines[start_index:end_index]

        return "\n".join(
            line.strip()
            for line in experience_lines
            if line.strip()
        )

    def extract_dates(self, text):
        """
        Extract date ranges from experience text.
        """

        pattern = (
            r"\b(?:"
            r"Jan(?:uary)?|"
            r"Feb(?:ruary)?|"
            r"Mar(?:ch)?|"
            r"Apr(?:il)?|"
            r"May|"
            r"Jun(?:e)?|"
            r"Jul(?:y)?|"
            r"Aug(?:ust)?|"
            r"Sep(?:t(?:ember)?)?|"
            r"Oct(?:ober)?|"
            r"Nov(?:ember)?|"
            r"Dec(?:ember)?"
            r")?"
            r"\s*"
            r"(?:19|20)\d{2}"
            r"\s*"
            r"(?:-|–|—|to)"
            r"\s*"
            r"(?:Present|Current|"
            r"(?:Jan(?:uary)?|"
            r"Feb(?:ruary)?|"
            r"Mar(?:ch)?|"
            r"Apr(?:il)?|"
            r"May|"
            r"Jun(?:e)?|"
            r"Jul(?:y)?|"
            r"Aug(?:ust)?|"
            r"Sep(?:t(?:ember)?)?|"
            r"Oct(?:ober)?|"
            r"Nov(?:ember)?|"
            r"Dec(?:ember)?)?"
            r"\s*"
            r"(?:19|20)\d{2}"
            r")\b"
        )

        matches = re.findall(
            pattern,
            text,
            flags=re.IGNORECASE
        )

        return matches

    def extract_years(self, text):
        """
        Extract years from experience text.
        """

        pattern = r"\b(?:19|20)\d{2}\b"

        years = re.findall(pattern, text)

        return list(dict.fromkeys(years))

    def extract_role(self, lines):
        """
        Try to identify a job title from experience lines.
        """

        for line in lines:

            clean_line = line.strip()

            lower_line = clean_line.lower()

            for keyword in self.ROLE_KEYWORDS:

                if keyword in lower_line:

                    return clean_line

        return None

    def extract_company(self, lines, role):
        """
        Try to identify the company name.

        Usually the company is located near the job title.
        """

        if not role:
            return None

        role_index = None

        for i, line in enumerate(lines):

            if line.strip() == role.strip():
                role_index = i
                break

        if role_index is None:
            return None

        # Check the lines immediately after the role
        for i in range(
            role_index + 1,
            min(role_index + 3, len(lines))
        ):

            candidate = lines[i].strip()

            if not candidate:
                continue

            # Ignore dates
            if re.search(
                r"(?:19|20)\d{2}",
                candidate
            ):
                continue

            return candidate

        return None

    def extract_description(self, lines, role, company):
        """
        Extract descriptive/bullet points from experience.
        """

        description_lines = []

        for line in lines:

            clean_line = line.strip()

            if not clean_line:
                continue

            if clean_line == role:
                continue

            if company and clean_line == company:
                continue

            # Ignore date lines
            if re.search(
                r"\b(?:19|20)\d{2}\b",
                clean_line
            ):
                continue

            description_lines.append(clean_line)

        return " ".join(description_lines)

    def extract_experience(self, text):
        """
        Extract structured work experience information.
        """

        experience_section = self.extract_experience_section(text)

        if not experience_section:
            return {
                "experiences": []
            }

        lines = experience_section.splitlines()

        role = self.extract_role(lines)

        company = self.extract_company(
            lines,
            role
        )

        dates = self.extract_dates(
            experience_section
        )

        years = self.extract_years(
            experience_section
        )

        description = self.extract_description(
            lines,
            role,
            company
        )

        experience = {
            "role": role,
            "company": company,
            "duration": dates[0] if dates else None,
            "years": years,
            "description": description
        }

        return {
            "experiences": [experience]
        }