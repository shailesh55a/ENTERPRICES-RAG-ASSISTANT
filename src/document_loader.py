from langchain_community.document_loaders import PyPDFLoader

from langchain_community.document_loaders import PyPDFLoader

def load_pdf(pdf_path):

    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    return documents

# reads uploaded PDF
# extract all text
# return document objects