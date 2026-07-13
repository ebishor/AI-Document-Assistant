from fastapi import UploadFile

from app.services.document_service import save_document
from app.services.pdf_service import extract_text
from app.services.chunk_service import split_text
from app.services.embedding_service import generate_embedding


def process_document(file: UploadFile):

    # Save PDF
    file_path = save_document(file)

    # Extract text
    text = extract_text(file_path)

    # Split into chunks
    chunks = split_text(text)

    # Generate embeddings
    embeddings = [generate_embedding(chunk) for chunk in chunks]

    return {
        "path": file_path,
        "text": text,
        "chunks": chunks,
        "embeddings": embeddings
    }