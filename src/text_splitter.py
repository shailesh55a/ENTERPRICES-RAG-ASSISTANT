from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_document(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    return chunks

# Large PDFs cannot fit directly into the model context.
# 100-page pdf
# split into chunks
# 1000 characters each