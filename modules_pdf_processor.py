"""
Module: pdf_processor.py
Handles reading PDF and text files using pure Python / PyPDF2 with fallback decoding
"""

import io
try:
    import PyPDF2
    PYPDF2_AVAILABLE = True
except ImportError:
    PYPDF2_AVAILABLE = False

def extract_text_from_pdf(uploaded_file) -> str:
    """Extracts text cleanly from an uploaded file stream"""
    filename = uploaded_file.name.lower()
    
    if filename.endswith(".txt") or filename.endswith(".md"):
        content = uploaded_file.read().decode("utf-8", errors="ignore")
        return content
        
    if filename.endswith(".pdf"):
        if PYPDF2_AVAILABLE:
            try:
                reader = PyPDF2.PdfReader(uploaded_file)
                extracted_pages = []
                for i, page in enumerate(reader.pages):
                    text = page.extract_text()
                    if text:
                        extracted_pages.append(f"--- Page {i+1} ---\n" + text)
                return "\n\n".join(extracted_pages)
            except Exception as e:
                return f"Error parsing PDF with PyPDF2: {str(e)}"
        else:
            # Fallback pure-python binary string sweep
            raw_bytes = uploaded_file.read()
            text = raw_bytes.decode("latin-1", errors="ignore")
            # Extract printable ascii streams
            import re
            readable = re.findall(r'[a-zA-Z0-9.,;:!?()\'\"/\-\s]{4,}', text)
            return "\n".join(readable[:500])
            
    return ""

def get_document_metrics(text: str) -> dict:
    words = len(text.split())
    chars = len(text)
    read_time = max(1, round(words / 200))
    return {
        "words": words,
        "chars": chars,
        "read_time": read_time
    }
