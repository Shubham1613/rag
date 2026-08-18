from app.services.embedding_service import model
from app.db.vector_db import search_similar
from app.db.redis_client import save_message, get_history
from app.services.llm_service import generate_answer


async def answer_query(question, session_id):

    query_embedding = model.encode(question)

    docs = search_similar(query_embedding)

    context = "\n".join(docs)

    history = get_history(session_id)

    prompt = f"""
You are a company knowledge assistant.

Answer ONLY using the provided context.

Context:
{context}

Chat History:
{history}

Question:
{question}

Answer:
"""

    answer = generate_answer(prompt)

    save_message(session_id, "user", question)
    save_message(session_id, "assistant", answer)

    return answer