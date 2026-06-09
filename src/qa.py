from src.embeddings import get_embeddings_model
from src.retriever import load_retriever
from src.rag_chain import build_rag_chain

def ask_question(question):

    embeddings = get_embeddings_model()

    retriever = load_retriever(embeddings)

    chain = build_rag_chain(retriever)

    result = chain.run(question)

    return result