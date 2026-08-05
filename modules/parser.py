import fitz
from docx import Document
from pathlib import Path
import re

class  ResumeParser:
    def __init__(self):
        pass
    def extract_pdf_text(self, file_path):
        
         file_path = Path(file_path)

         if not file_path.exists():
             raise FileNotFoundError(f"{file_path} not found")
         document = fitz.open(file_path)

         text = ""

         for page in document:
             text += page.get_text()

         document.close()
         return text   

    def extract_docx_text(self, file_path):

        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"{file_path} not found")

        document = Document(file_path)

        text = ""

        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"

        return text    

    def clean_text(self , text):

        text = re.sub(r"\s+", " ", text)
        text = text.strip()

        return text
    def parser_resume(self , file_path):

        file_path = Path(file_path)

        suffix = file_path.suffix.lower()

        if suffix == ".pdf":
            text = self.extract_pdf_text(file_path)

        elif suffix == ".docx":
            text = self.extract_docx_text(file_path)

        else:
            raise ValueError("Unsupported file format.")

        return self.clean_text(text)
    
    
                
