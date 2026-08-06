import pandas as pd
from pathlib import Path
import re

class SkillExtractor:

    def __init__(self, skills_file):
        self.skills_file = Path(skills_file)
        self.skills_df = self.load_skills()

    def load_skills(self):

        if not self.skills_file.exists():
            raise FileNotFoundError(
                f"{self.skills_file} not found."
            )
        
        return pd.read_csv(self.skills_file)

    def extract_skills(self, text):

        text = text.lower()

        matched_skills = []

        for _, row in self.skills_df.iterrows():

            skill = row["skill"]
            category = row["category"]

            pattern = rf"\b{re.escape(skill.lower())}\b"

            if re.search(pattern, text):

                matched_skills.append({
                    "skill":skill,
                    "category":category
                })
        return matched_skills
            
        