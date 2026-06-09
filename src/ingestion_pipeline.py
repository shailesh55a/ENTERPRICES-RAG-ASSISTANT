from src.document_loader import load_pdf
from src.text_splitter import split_document
from src.embeddings import get_embeddings_model
from src.vector_store import create_vector_store

def process_pdf(pdf_path):

    documents = load_pdf(pdf_path)

    chunks = split_document(documents)

    embeddings = get_embeddings_model()

    create_vector_store(
        chunks,
        embeddings
    )

    return True