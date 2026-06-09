from langchain_community.vectorstores import FAISS

def load_retriever(embeddings):

    db = FAISS.load_local(
        "vectorstore",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db.as_retriever()

# retrieves relevant chunks before sending to LLM.