from modules.parser import ResumeParser
from modules.extractors.information_extractor import InformationExtractor

parser = ResumeParser()
extractor = InformationExtractor()

text = parser.parser_resume("D:\\Downloads\\Yash_Pandey_Resume.pdf")

info = extractor.extract_information(text)

print(info)