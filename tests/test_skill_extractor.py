from modules.parser import ResumeParser
from modules.extractors.skill_extractor import SkillExtractor

parser = ResumeParser()

extractor = SkillExtractor("datasets/skills/skills.csv")

text = parser.parser_resume("D:\\Downloads\\Yash_Pandey_Resume.pdf")

skills = extractor.extract_skills(text)

print(skills)