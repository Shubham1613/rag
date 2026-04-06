                +------------------+
User Question → |   FastAPI API    |
                +---------+--------+
                          |
                          v
                +------------------+
                |  Redis (Chat)    |
                | Conversation ctx |
                +------------------+
                          |
                          v
                +------------------+
                | Vector Database  |
                | (PGVector/Chroma)|
                +------------------+
                          |
                          v
               +--------------------+
               | Embedding Service  |
               | OpenAI / HF Model  |
               +--------------------+
                          |
                          v
               +--------------------+
               |   LLM (GPT etc.)   |
               +--------------------+


Flow :
        Upload Document
            ↓
        Extract Text
            ↓
        Chunk Text
            ↓
        Generate Embeddings
            ↓
        Store in Vector DB