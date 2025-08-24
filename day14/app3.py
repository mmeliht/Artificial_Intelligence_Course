import streamlit as st
import ollama
import tempfile

def main():
    st.title("Görüntüden Metin Çıkarma Uygulaması")
    
    uploaded_file = st.file_uploader("Bir görüntü yükleyin (örn: typewritten.png)", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        # Geçici dosya oluştur
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_file_path = temp_file.name
        
        st.image(uploaded_file, caption='Yüklenen Görüntü', use_column_width=True)
        
        if st.button("Metni Çıkar"):
            res = ollama.chat(
                model='llama3.2-vision:11b',
                messages=[{
                    'role': 'user',
                    'content': 'Extract the exact text as it appears on this image, nothing less nothing more',
                    'images': [temp_file_path]
                }]
            )
            st.write(res['message']['content'])

if __name__ == "__main__":
    main()