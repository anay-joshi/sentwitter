import nltk
import uvicorn
import utils as utils
from fastapi import FastAPI
from pydantic import BaseModel
from classify import remove_noise
from nltk.tokenize import word_tokenize

app = FastAPI()
classifier = utils.load_model()
# nltk.download("punkt")
# nltk.download("wordnet")
# nltk.download("stopwords")
# nltk.download("averaged_perceptron_tagger")


class Tweet(BaseModel):
    tweet: str


@app.get("/")
def read_root():
    return {"message": "Welcome to sentiment classifier API"}


@app.post("/api")
def analyse_tweet(tweet: Tweet):
    custom_tokens = remove_noise(word_tokenize(tweet.tweet))
    result = classifier.classify(dict([token, True] for token in custom_tokens))
    return {"sentiment": result}


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", log_level="info")

