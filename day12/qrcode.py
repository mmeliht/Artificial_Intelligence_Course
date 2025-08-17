import streamlit as st
import qrcode
from PIL import Image
st.title('QR Code Generator')
data = st.text_input('Enter text or URL')

if data:
    qr = qrcode.make(data)
    st.image(qr)



## Bu projede hata var o yüzden çalışmıyor.




