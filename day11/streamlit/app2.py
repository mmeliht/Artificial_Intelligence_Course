import streamlit as st
import pickle
st.title('Tecrübe, yazılı sınav ve mülakata göre maaş tahmini :heavy_dollar_sign:')
model=pickle.load(open('maas.pkl','rb'))
tecrube=st.number_input('tecrube',1,10)
yazili=st.number_input('yazili',1,10)
sozlu=st.number_input('sozzlu',1,10)
if st.button('tahmin et'):
    tahmin=model.predict([[tecrube, yazili, sozlu]])
    tahmin=round(tahmin[0][0],2)
    st.success(f'YZ tahmin edilen maasiniz:{tahmin}')

'''
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

'''
