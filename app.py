import streamlit as st
from classify import classify
import pickle
import config
import tweepy as tw
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import nltk

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

auth = tw.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

f = open('sentiment_model.pickle', 'rb')
classifier = pickle.load(f)
f.close()

st.title('Twitter Live Sentiment Visualizer')

st.sidebar.title('Enter a hashtag')
hashtag = st.sidebar.text_input('hashtag', 'trump')
date = st.sidebar.date_input('Analyse tweets from,', datetime.date(2020, 6, 18))

if st.sidebar.button('Live analysis', key='analyse'):
    pos_count = 0
    neg_count = 0
    tweets_count = 0
    st.subheader(f'Analysing #{hashtag} from {date}')
    d = {"Positive": [pos_count], "Negative": [neg_count]}
    df = pd.DataFrame(data=d)
    # st.write(df)
    hashtag = f'#{hashtag}'
    tweets = tw.Cursor(
        api.search,
        q=hashtag,
        lang='en',
        since=date
    ).items()
    chart = st.line_chart(df)
    # chart2 = st.bar_chart(df.tail(1))
    for idx, tweet in enumerate(tweets):
        tweets_count += 1
        output = classify(tweet.text, classifier)
        if output == "Negative":
            neg_count += 1
        elif output == "Positive":
            pos_count += 1
        # st.write(neg_count, pos_count)
        df2 = pd.DataFrame({"Positive": [pos_count], "Negative": [neg_count]})
        chart.add_rows(df2)
        # chart2.add_rows(df2)
        # st.pyplot()
    st.success('Tweets classified')
        