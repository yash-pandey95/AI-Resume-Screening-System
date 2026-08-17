from modules.resume_processor import ResumeProcessor
from modules.job_processor import JobProcessor
from modules.matching_engine import MatchingEngine

from pprint import pprint


# ==========================================
# 1. Process Resume
# ==========================================

resume_processor = ResumeProcessor(
    "datasets/skills/skills.csv",
    "datasets/education/degrees.csv"
)

resume = resume_processor.process_resume(
    "D:\\Downloads\\Yash_Pandey_Resume.pdf"
)


# ==========================================
# 2. Process Job Description
# ==========================================

job_description = """
Machine Learning Engineer

We are looking for a Machine Learning Engineer
with strong experience in Python, Pandas, NumPy,
Scikit-Learn, TensorFlow and SQL.

The candidate should have 2+ years of experience
in machine learning and data preprocessing.

Experience with Docker is preferred.
"""


job_processor = JobProcessor(
    "datasets/skills/skills.csv"
)

job = job_processor.process_job(
    job_description
)


# ==========================================
# 3. Match Resume with Job
# ==========================================

matching_engine = MatchingEngine()

matching_result = matching_engine.match_skills(
    resume["skills"],
    job["required_skills"]
)


# ==========================================
# 4. Display Results
# ==========================================

print("\n")
print("=" * 60)
print("RESUME VS JOB MATCHING")
print("=" * 60)

print("\nJOB TITLE:")
print(job["job_title"])

print("\nMATCHED SKILLS:")
for skill in matching_result["matched_skills"]:
    print("✓", skill)

print("\nMISSING SKILLS:")
for skill in matching_result["missing_skills"]:
    print("✗", skill)

print("\nSKILL MATCH:")
print(
    f"{matching_result['skill_match_percentage']}%"
)

print("\n")
print("=" * 60)