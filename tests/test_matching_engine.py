from modules.matching_engine import MatchingEngine
from pprint import pprint


# -----------------------------
# Sample Resume Skills
# -----------------------------

resume_skills = [
    {
        "skill": "Python",
        "category": "Programming Language"
    },
    {
        "skill": "Pandas",
        "category": "Data Analysis"
    },
    {
        "skill": "NumPy",
        "category": "Data Analysis"
    },
    {
        "skill": "SQL",
        "category": "Database"
    },
    {
        "skill": "Machine Learning",
        "category": "Machine Learning"
    }
]


# -----------------------------
# Job Required Skills
# -----------------------------

required_skills = [
    {
        "skill": "Python",
        "category": "Programming Language"
    },
    {
        "skill": "Pandas",
        "category": "Data Analysis"
    },
    {
        "skill": "NumPy",
        "category": "Data Analysis"
    },
    {
        "skill": "SQL",
        "category": "Database"
    },
    {
        "skill": "Machine Learning",
        "category": "Machine Learning"
    },
    {
        "skill": "TensorFlow",
        "category": "Machine Learning"
    },
    {
        "skill": "Docker",
        "category": "DevOps"
    }
]


# -----------------------------
# Matching
# -----------------------------

engine = MatchingEngine()

result = engine.match_skills(
    resume_skills,
    required_skills
)


# -----------------------------
# Output
# -----------------------------

pprint(
    result,
    sort_dicts=False
)