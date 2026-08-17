from modules.job_processor import JobProcessor
from pprint import pprint


job_description = """
Machine Learning Engineer

We are looking for a Machine Learning Engineer
with strong experience in Python, Pandas, NumPy,
Scikit-Learn, TensorFlow and SQL.

The candidate should have 2+ years of experience
in machine learning and data preprocessing.
"""


processor = JobProcessor(
    "datasets/skills/skills.csv"
)


job = processor.process_job(
    job_description
)


pprint(
    job,
    sort_dicts=False
)