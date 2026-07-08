from fastapi import UploadFile

from app.services.document_service import save_document
from app.services.pdf_service import extract_text
from app.services.chunk_service import split_text


def process_document(file: UploadFile):

    # Step 1 - Save file
    file_path = save_document(file)

    # Step 2 - Extract text
    text = extract_text(file_path)

    # Step 3 - Split into chunks
    chunks = split_text(text)

    return {
        "path": file_path,
        "text": text,
        "chunks": chunks
    }