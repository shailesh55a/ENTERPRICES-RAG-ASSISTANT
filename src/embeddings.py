from langchain_community.embeddings import HuggingFaceEmbeddings

def get_embeddings_model():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return embeddings

# embeddings convert text into vectors.
# what is ai?
# conversions [0.23, 0.44, 0.11, ...]