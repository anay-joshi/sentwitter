import utils as utils
from fastapi import FastAPI
from pydantic import BaseModel
from classify import remove_noise
from nltk.tokenize import word_tokenize

app = FastAPI()
classifier = utils.load_model()


class Tweet(BaseModel):
    tweet: str


@app.post("/api")
def analyse_tweet(tweet: Tweet):
    custom_tokens = remove_noise(word_tokenize(tweet.tweet))
    result = classifier.classify(dict([token, True] for token in custom_tokens))
    return {"sentiment": result}
