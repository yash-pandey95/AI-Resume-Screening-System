from pathlib import Path
from models.resume_model import ResumeModel

from modules.parser import ResumeParser
from modules.extractors.information_extractor import InformationExtractor
from modules.extractors.skill_extractor import SkillExtractor

class ResumeProcessor:

    def __init__(self, skills_file):
        self.parser = ResumeParser()
        self.information_extractor = InformationExtractor()
        self.skill_extractor = SkillExtractor(skills_file)

    def process_resume(self, file_path):

        file_path = Path(file_path)
        resume = ResumeModel.create()

        resume["metadata"]["file_name"] = file_path.name
        resume["metadata"]["file_type"] = file_path.suffix

        text = self.parser.parser_resume(file_path)
        resume["resume_text"] = text

        personal_information = self.information_extractor.extract_information(text)
        resume["personal_information"] = personal_information

        skills = self.skill_extractor.extract_skills(text)
        resume["skills"] = skills

        return resume