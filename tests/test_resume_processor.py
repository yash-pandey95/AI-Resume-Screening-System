from modules.resume_processor import ResumeProcessor
from pprint import pprint

processor = ResumeProcessor("datasets/skills/skills.csv","datasets/education/degrees.csv" )

resume = processor.process_resume("D:\\Downloads\\Yash_Pandey_Resume.pdf")

pprint(resume , sort_dicts=False)