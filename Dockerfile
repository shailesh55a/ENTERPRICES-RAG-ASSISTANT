FROM python:3.11

WORKDIR /app

COPY . .

ENV PYTHONPATH=/app

RUN pip install -r requirements.txt

CMD ["streamlit","run","streamlit_app/app.py","--server.address=0.0.0.0","--server.port=8501"]   