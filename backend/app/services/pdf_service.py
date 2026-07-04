import fitz


def extract_text(pdf_path: str) -> str:
    """
    Extract all text from a PDF.
    """

    document = fitz.open(pdf_path)   #open pdf document

    text = ""

    for page in document:
        text += page.get_text()     #extract text from each page and append to the text variable

    document.close()

    return text