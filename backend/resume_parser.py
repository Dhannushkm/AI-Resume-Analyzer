import pdfplumber
import pytesseract
from pdf2image import convert_from_path
import os

# Tell pytesseract where Tesseract is installed
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_pdf(file_path):
    text = ""

    # -------- Try normal text extraction first --------
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    # -------- If no text found, use OCR --------
    if len(text.strip()) == 0:
        print("No text layer found. Switching to OCR...")

        images = convert_from_path(
            file_path,
            poppler_path=r"C:\poppler-25.12.0\Library\bin"
            )

        for image in images:
            ocr_text = pytesseract.image_to_string(image)
            text += ocr_text + "\n"

    return text