FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN python3 -m nltk.downloader punkt
RUN python3 -m nltk.downloader wordnet
RUN python3 -m nltk.downloader stopwords
RUN python3 -m nltk.downloader averaged_perceptron_tagger

# RUN bash setup.sh

EXPOSE 8000

CMD ["uvicorn", "server:app"]