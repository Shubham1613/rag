from app.utils.pdf_parser import extract_text_from_pdf
from app.utils.chunking import chunk_text
from app.services.embedding_service import generate_embeddings
from app.db.vector_db import store_embeddings


async def ingest_document(file):

    content = await file.read()

    if file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(content)

    else:
        text = content.decode()

    chunks = chunk_text(text)

    embeddings = generate_embeddings(chunks)

    store_embeddings(chunks, embeddings)