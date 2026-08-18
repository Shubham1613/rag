import chromadb

client = chromadb.Client()

collection = client.get_or_create_collection("knowledge_base")


def store_embeddings(chunks, embeddings):

    ids = [str(i) for i in range(len(chunks))]

    collection.add(
        documents=chunks,
        embeddings=embeddings.tolist(),
        ids=ids
    )


def search_similar(query_embedding, top_k=5):

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results["documents"][0]