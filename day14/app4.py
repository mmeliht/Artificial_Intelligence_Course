import streamlit as st
import PyPDF2
import ollama

def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text() + '\n'
    return text

def main():
    st.title("PDF Belgesi Yükleyin ve Sohbet Edin")
    
    uploaded_file = st.file_uploader("PDF belgesi yükleyin", type=["pdf"])
    
    if uploaded_file is not None:
        # PDF içeriğini oku
        text = read_pdf(uploaded_file)
        
        if text:
            st.subheader("PDF İçeriği:")
            st.write(text)
            
            user_input = st.text_input("Belge hakkında bir soru sorun:")
            
            if st.button("Sohbet Et"):
                res = ollama.chat(
                    model='llama3.2-vision:11b-instruct-q8_0',
                    messages=[{
                        'role': 'user',
                        'content': user_input,
                        'context': text
                    }]
                )
                st.write(res['message']['content'])
        else:
            st.write("PDF'den metin çıkarılamadı.")

if __name__ == "__main__":
    main()