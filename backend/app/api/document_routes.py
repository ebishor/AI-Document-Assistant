from fastapi import APIRouter, UploadFile, File

from app.processors.document_processor import process_document

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.post("/upload")
def upload_document(file: UploadFile = File(...)):

    result = process_document(file)

    return {
        "filename": file.filename,
        "saved_to": result["path"],
        "characters": len(result["text"]),
        "number_of_chunks": len(result["chunks"]),
        "first_chunk": result["chunks"][0] if result["chunks"] else ""
    }