# Sentiment Analiz
import streamlit as st
from textblob import TextBlob
st.title('Sentiment Analyzer')
txt=st.text_area('Enter Text')
if txt:
    polarity=TextBlob(txt).sentiment.polarity
    if polarity> 0.10:
        sentiment='Positive'
    elif polarity <-0.10:
        sentiment='Negative'
    else:
        sentiment='Neutral'
    st.write("sentimens is :",sentiment)

