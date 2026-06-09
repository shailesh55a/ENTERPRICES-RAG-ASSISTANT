# 📚 Enterprise RAG Assistant

An AI-powered Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions based on their content. The system extracts information from uploaded documents, stores embeddings in a vector database, retrieves relevant context, and generates accurate answers using a Large Language Model (LLM).

---

# 🚀 Features

- Upload PDF documents
- Extract text from PDFs
- Split documents into chunks
- Generate embeddings using Sentence Transformers
- Store embeddings in FAISS Vector Database
- Semantic Search & Retrieval
- Context-Aware Question Answering
- Groq LLM Integration
- Chat-Based Streamlit Interface
- Dockerized Application
- FastAPI Backend
- Render Deployment Ready

---

# 🏗️ Architecture

```text
PDF Upload
    ↓
Document Loader
    ↓
Text Chunking
    ↓
Embeddings
    ↓
FAISS Vector Store
    ↓
Retriever
    ↓
Groq LLM
    ↓
Answer Generation
```

---

# 🛠️ Tech Stack

### Frontend

- Streamlit

### Backend

- FastAPI

### AI/LLM

- LangChain
- Groq (Llama Models)

### Vector Database

- FAISS

### Embeddings

- Sentence Transformers
- all-MiniLM-L6-v2

### Deployment

- Docker
- GitHub
- Render

### Programming Language

- Python

---

# 📂 Project Structure

```text
enterprise-rag-assistant/

│
├── api/
│   └── main.py
│
├── src/
│   ├── document_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── rag_chain.py
│   ├── qa.py
│   ├── utils.py
│   └── __init__.py
│
├── streamlit_app/
│   └── app.py
│
├── uploads/
├── vectorstore/
│
├── Dockerfile
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/enterprise-rag-assistant.git

cd enterprise-rag-assistant
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

# ▶️ Run Application

## Streamlit Frontend

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## FastAPI Backend

```bash
uvicorn api.main:app --reload
```

Open:

```text
http://localhost:8000/docs
```

---

# 🐳 Docker Setup

## Build Docker Image

```bash
docker build -t enterprise-rag-assistant .
```

---

## Run Docker Container

```bash
docker run -p 8501:8501 enterprise-rag-assistant
```

---

## Open Application

```text
http://localhost:8501
```

---

# ☁️ Render Deployment

## Step 1: Push Project to GitHub

```bash
git add .

git commit -m "Enterprise RAG Assistant"

git push origin main
```

---

## Step 2: Create Render Account

Visit:

```text
https://render.com
```

Sign in using GitHub.

---

## Step 3: Create New Web Service

- Click **New +**
- Select **Web Service**
- Connect GitHub Repository
- Select `enterprise-rag-assistant`

---

## Step 4: Configure Deployment

### Name

```text
enterprise-rag-assistant
```

### Environment

```text
Docker
```

### Branch

```text
main
```

### Region

```text
Singapore
```

---

## Step 5: Add Environment Variables

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

## Step 6: Deploy

Click:

```text
Create Web Service
```

Render will:

```text
Build Docker Image
↓
Install Dependencies
↓
Start Application
↓
Generate Public URL
```

---

## Step 7: Access Application

Example:

```text
https://enterprise-rag-assistant.onrender.com
```

---

# 📖 How It Works

### Step 1

User uploads PDF document.

### Step 2

Document Loader extracts text.

### Step 3

Text Splitter divides text into chunks.

### Step 4

Embedding Model converts chunks into vectors.

### Step 5

Vectors are stored inside FAISS.

### Step 6

User asks a question.

### Step 7

Retriever fetches relevant chunks.

### Step 8

Groq LLM generates an answer using retrieved context.

### Step 9

Answer is displayed in Streamlit UI.

---

# 📸 Example Questions

```text
What is Artificial Intelligence?

What is Machine Learning?

What is MLOps?

What is FAISS?

What does RAG stand for?

What tool is used for containerization?
```

---

# 🎯 Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- LangChain Framework
- Vector Databases (FAISS)
- NLP Pipelines
- Semantic Search
- Prompt Engineering
- FastAPI Development
- Streamlit Development
- Docker Containerization
- Git & GitHub
- Render Deployment
- Python Development

---

# 🔮 Future Enhancements

- Multiple PDF Upload Support
- Source Citations
- PostgreSQL Integration
- User Authentication
- Chat History Database
- Docker Compose
- CI/CD with GitHub Actions
- Kubernetes Deployment
- Multi-User Support

---

# 👨‍💻 Author

**Shailesh Bahirat**

BSc Artificial Intelligence & Machine Learning

---