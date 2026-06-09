from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():

    return {
        "message":"Enterprice RAG Assistant Running"
    }
