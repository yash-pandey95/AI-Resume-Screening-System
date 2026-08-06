import re

class InformationExtractor:

    def __init__(self):
        pass

    def extract_email(self, text):

        pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

        match = re.search(pattern, text)

        if match:
            return match.group()

        return None

    def extract_phone(self, text):

        pattern = r"(?:\+91[\-\s]?)?[6-9]\d{9}"

        match = re.search(pattern,text)

        if match:
            return match.group()

        return None

    def extract_linkedin(self, text):

        pattern = r"(https?://)?(www\.)?linkedin\.com/in/[A-Za-z0-9_-]+"

        match = re.search(pattern, text)

        if match:
            return match.group()

        return None

    def extract_github(self, text):

        pattern = r"(https?://)?(www\.)?github\.com/[A-Za-z0-9_-]+"

        match = re.search(pattern, text)

        if match:
            return match.group()
        return None

    def extract_name(self, text):
        lines = text.split()

        if len(lines) >= 2:
            return lines[1] + " "+ lines[2]
        return None

    
    def extract_information(self,text):

        return{
            "name": self.extract_name(text),
            "email": self.extract_email(text),
            "phone": self.extract_phone(text),
            "linkedin": self.extract_linkedin(text),
            "github": self.extract_github(text)
        }