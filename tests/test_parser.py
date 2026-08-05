from modules.parser import ResumeParser

parser = ResumeParser()

resume_text = parser.parser_resume("D:\\Downloads\\Yash_Pandey_Resume.pdf")

print("=" * 50)
print("Extracted Resume Text")
print("=" * 50)
print(resume_text)