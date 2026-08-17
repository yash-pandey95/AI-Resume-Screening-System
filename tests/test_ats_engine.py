from modules.resume_processor import ResumeProcessor
from modules.job_processor import JobProcessor
from modules.matching_engine import MatchingEngine
from modules.ats_engine import ATSEngine


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
# 2. Process Job
# ==========================================

job_description = """
Machine Learning Engineer

We are looking for a Machine Learning Engineer
with strong experience in Python, Pandas, NumPy,
Scikit-Learn, TensorFlow and SQL.

The candidate should have 2+ years of experience
in machine learning and data preprocessing.

Experience with Docker is preferred.

Candidates should have a Bachelor's degree
in Computer Science, Computer Engineering,
Machine Learning or a related field.
"""


job_processor = JobProcessor(
    "datasets/skills/skills.csv"
)

job = job_processor.process_job(
    job_description
)


# ==========================================
# 3. Skill Matching
# ==========================================

matching_engine = MatchingEngine()

matching_result = matching_engine.match_skills(
    resume["skills"],
    job["required_skills"]
)


# ==========================================
# 4. ATS Scoring
# ==========================================

ats_engine = ATSEngine()

ats_result = ats_engine.calculate_score(
    resume,
    job,
    matching_result
)


# ==========================================
# 5. Display
# ==========================================

print("\n")
print("=" * 60)
print("ATS RESUME SCREENING RESULT")
print("=" * 60)

print(
    f"\nOverall ATS Score: "
    f"{ats_result['overall_score']}/100"
)

print(
    f"\nSkill Match: "
    f"{ats_result['skill_match']}%"
)

print(
    f"Education Match: "
    f"{ats_result['education_match']}%"
)

print(
    f"Experience Match: "
    f"{ats_result['experience_match']}%"
)

print(
    f"Keyword Match: "
    f"{ats_result['keyword_match']}%"
)

print("\nMatched Skills:")

for skill in matching_result["matched_skills"]:
    print("  ✓", skill)

print("\nMissing Skills:")

for skill in matching_result["missing_skills"]:
    print("  ✗", skill)

print("\n")
print("=" * 60)