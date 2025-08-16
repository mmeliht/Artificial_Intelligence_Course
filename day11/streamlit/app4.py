import streamlit as st
from gtts import gTTS
st.title('Text to Speech')
text=st.text_area('Enter text')
if text:
    tts=gTTS(text)
    tts.save('ses.mp3')
    ses=open('ses.mp3','rb')
    st.audio(ses.read())