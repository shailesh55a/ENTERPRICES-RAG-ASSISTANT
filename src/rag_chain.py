import os 

from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
load_dotenv()

def build_rag_chain(retriever):

    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile"
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"
    )

    return qa_chain