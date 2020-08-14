FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8501

COPY . .

CMD ["streamlit", "run", "tweets.py"]