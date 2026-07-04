from pathlib import Path
import shutil
from fastapi import UploadFile

from app.services.pdf_service import extract_text
from app.services.chunk_service import split_text

UPLOAD_DIR = Path("app/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def save_document(file: UploadFile):

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(str(file_path))

    chunks = split_text(text)

    return {
        "path": str(file_path),
        "text": text,
        "chunks": chunks
    }