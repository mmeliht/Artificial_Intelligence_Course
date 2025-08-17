import streamlit as st
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import cv2
model=load_model('skin_cancer_tl_v2')
def process_image(img):
    img=img.resize((224,224))
    img=np.array(img)
    img=img/255.0
    img=np.expand_dims(img,axis=0)
    return img
st.title("kanser resmi siniflandirma :cancer:")
st.write("resim sec ve model kanser olup olmadigini tahmin etsin")
file=st.file_uploader('bir resim sec',type=['jpg','jpeg','png'])
if file is not None:
    img=Image.open(file)
    st.image(img,caption='yuklenen resim')
    image= process_image(img)
    prediction=model.predict(image)
    predicted_class=np.argmax(prediction)
    
    class_names=['Kanser Degil','Kanser']
    st.write(class_names[predicted_class])