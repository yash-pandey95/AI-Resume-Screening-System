import fitz
from docx import Document
from pathlib import Path
import re

class  ResumeParser:
    def __init__(self):
        pass
    def extract_pdf_text(self, file_path):
         """extract text from pdf
      """
         file_path = Path(file_path)

         if not file_path.exists():
             raise FileNotFoundError(f"{file_path} not found")
         document = fitz.open(file_path)

         text = ""

         for page in document:
             text += page.get_text()

         document.close()
         return text    
