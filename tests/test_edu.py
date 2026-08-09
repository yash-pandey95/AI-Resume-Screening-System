from modules.parser import ResumeParser
from modules.extractors.education_extractor import EducationExtractor
from pprint import pprint


parser = ResumeParser()

extractor = EducationExtractor(
    "datasets/education/degrees.csv"
)

text = parser.parser_resume(
    "D:\\Downloads\\Yash_Pandey_Resume.pdf"
)

education = extractor.extract_education(text)

pprint(education, sort_dicts=False)