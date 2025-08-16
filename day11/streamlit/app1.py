import streamlit as st

st.title("MLOps Spreamlit Apps :flag-tr:") # :flag-tr: yerine iconun adını yazarsak o gelir


import streamlit as st
import pandas as pd
import plotly.express as px
st.title("MLOps Spreatmlit Apps :balloon:")
st.balloons()
df=pd.read_csv('data/prog_languages_data.csv')
fig=px.pie(df, values='Sum')
st.plotly_chart(fig)
fig2=px.bar(df,x='lang',y='Sum')
st.plotly_chart(fig2)
st.radio('Medeni Durumu',('Evli','Bekar','Dul','Nisanli'))
st.selectbox('Bildiginiz Programlama dilleri',['C++','Python','ASP','Visual Basic','C','Q#','Java','julia','HTML','PHP'])
st.multiselect('Bildiginiz Programlama dilleri',['C++','Python','ASP','Visual Basic','C','Q#','Java','julia','HTML','PHP'])
st.divider()
df=pd.read_csv('data/iris.csv')
st.write(df)
st.area_chart(df)



'''
st.date_input('tarih_sec')
st.time_input('saat_sec')

# st.camera.input('') bu tam çalışmadı . doğrudan kameradan görüntüyü web sitesine aktarıyor.

st.video("data/secret_of_success.mp4")

st.image("data/image_01.jpg")

'''

