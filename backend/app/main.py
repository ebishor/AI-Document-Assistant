from fastapi import FastAPI

from app.api.document_routes import router as document_router

app = FastAPI(
    title="AI Document Assistant",
    version="1.0.0"
)

app.include_router(document_router)

@app.get("/")
def home():
    return {
        "message": "AI Document Assistant API"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }