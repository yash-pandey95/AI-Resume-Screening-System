class ResumeModel:

    @staticmethod
    def create():
        return {
            "metadata": {
                "file_name": "",
                "file_type": "",
                "pages": 0,
                "status": "success"
            },

            "resume_text": "",

            "personal_information": {
                "name": "",
                "email": "",
                "phone": "",
                "linkedin": "",
                "github": ""
            },

            "skills": [],

            "education": [],

            "experience": [],

            "projects": [],

            "certifications": [],

            "ats": {
                "score": None,
                "matched_skills": [],
                "missing_skills": []
            },

            "ml": {
                "predicted_role": None,
                "confidence": None
            }
        }