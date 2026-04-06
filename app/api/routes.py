from fastapi import APIRouter, UploadFile, File
from app.services.ingestion_service import ingest_document
from app.services.rag_service import answer_query

router = APIRouter()

@router.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):
    
    await ingest_document(file)

    return {"message": "Document indexed successfully"}


@router.post("/chat/query")
async def query(question: str, session_id: str):

    response = await answer_query(question, session_id)

    return {"answer": response}