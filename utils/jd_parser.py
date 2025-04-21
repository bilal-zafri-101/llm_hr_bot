import fitz  # PyMuPDF
import io
from typing import Union

def extract_text_from_pdf(file: Union[io.BytesIO, str]) -> str:
    try:
        doc = fitz.open(stream=file.read(), filetype="pdf") if isinstance(file, io.BytesIO) else fitz.open(file)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text.strip()
    except Exception as e:
        return f"[ERROR] JD PDF parsing failed: {e}"

def extract_text_from_txt(file: Union[io.BytesIO, str]) -> str:
    try:
        if isinstance(file, io.BytesIO):
            return file.read().decode('utf-8').strip()
        else:
            with open(file, 'r', encoding='utf-8') as f:
                return f.read().strip()
    except Exception as e:
        return f"[ERROR] JD TXT parsing failed: {e}"

def parse_jd(file: Union[io.BytesIO, str], filename: str = "") -> str:
    filename = filename.lower()
    if filename.endswith(".pdf"):
        return extract_text_from_pdf(file)
    elif filename.endswith(".txt"):
        return extract_text_from_txt(file)
    else:
        return "[ERROR] Unsupported JD format. Use .txt or .pdf."
