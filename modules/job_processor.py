from modules.extractors.job_extractor import JobExtractor


class JobProcessor:
    """
    Coordinates job description processing.
    """

    def __init__(self, skills_file):

        self.job_extractor = JobExtractor(skills_file)

    def process_job(self, job_description):
        """
        Process a job description and return
        structured job information.
        """

        if not isinstance(job_description, str):
            raise TypeError(
                "Job description must be a string."
            )

        if not job_description.strip():
            raise ValueError(
                "Job description cannot be empty."
            )

        job = self.job_extractor.extract_job(
            job_description
        )

        return job