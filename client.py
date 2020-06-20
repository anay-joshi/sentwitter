import streamlit as st
from classify import classify
import pickle

f = open('sentiment_model.pickle', 'rb')
classifier = pickle.load(f)
f.close()

st.title('Twitter Live Sentiment Visualizer')

st.sidebar.title('Enter a hashtag')
hashtag = st.sidebar.text_input('hashtag', 'trump')

if st.sidebar.button('Live analysis', key='analyse'):
    st.subheader(f'Analysing #{hashtag}')