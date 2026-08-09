from modules.parser import ResumeParser
from modules.extractors.experience_extractor import ExperienceExtractor
from pprint import pprint


parser = ResumeParser()

extractor = ExperienceExtractor()

text = parser.parser_resume(
    "D:\\Downloads\\Yash_Pandey_Resume.pdf"
)

experience = extractor.extract_experience(text)

pprint(
    experience,
    sort_dicts=False
)