import streamlit as st

from src.utils import save_uploaded_file
from src.ingestion_pipeline import process_pdf
from src.qa import ask_question

# ----------------------------------
# Page Configuration
# ----------------------------------

st.set_page_config(
    page_title="Enterprise RAG Assistant",
    page_icon="📚",
    layout="wide"
)

# ----------------------------------
# Session State
# ----------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pdf_processed" not in st.session_state:
    st.session_state.pdf_processed = False

# ----------------------------------
# Title
# ----------------------------------

st.title("📚 Enterprise RAG Assistant")

st.markdown(
    """
    Upload a PDF document and ask questions about its content.
    """
)

# ----------------------------------
# Sidebar
# ----------------------------------

with st.sidebar:

    st.header("Upload PDF")

    uploaded_pdf = st.file_uploader(
        "Choose PDF File",
        type=["pdf"]
    )

    if uploaded_pdf:

        if st.button("Process PDF"):

            with st.spinner("Processing PDF..."):

                try:

                    pdf_path = save_uploaded_file(
                        uploaded_pdf
                    )

                    process_pdf(pdf_path)

                    st.session_state.pdf_processed = True

                    st.success(
                        "PDF processed successfully!"
                    )

                except Exception as e:

                    st.error(
                        f"Error: {str(e)}"
                    )

# ----------------------------------
# Main Chat Section
# ----------------------------------

st.subheader("Ask Questions")

question = st.text_input(
    "Enter your question:"
)

if st.button("Submit Question"):

    if not st.session_state.pdf_processed:

        st.warning(
            "Please upload and process a PDF first."
        )

    elif question.strip() == "":

        st.warning(
            "Please enter a question."
        )

    else:

        try:

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            with st.spinner("Generating answer..."):

                answer = ask_question(
                    question
                )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": answer
                }
            )

        except Exception as e:

            st.error(
                f"Error: {str(e)}"
            )

# ----------------------------------
# Chat History
# ----------------------------------

st.subheader("Chat History")

for message in st.session_state.messages:

    if message["role"] == "user":

        st.chat_message("user").write(
            message["content"]
        )

    else:

        st.chat_message("assistant").write(
            message["content"]
        )

# ----------------------------------
# Clear Chat
# ----------------------------------

if st.button("Clear Chat"):

    st.session_state.messages = []

    st.rerun()
