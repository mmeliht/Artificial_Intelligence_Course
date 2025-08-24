import streamlit as st
import base64
from openai import OpenAI

def main():
    st.title("Görüntü ile Sohbet Uygulaması")

    uploaded_file = st.file_uploader("Resminizi yükleyin (örn: PNG, JPG)", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        # Yüklenen resmi göster
        st.image(uploaded_file, caption="Yüklenen Resim", use_column_width=True)

        user_input = st.text_input("Bu resim hakkında bir soru sorun:")

        if st.button("Sohbet Et"):
            # Resmi base64 formatına çevir
            image_bytes = uploaded_file.read()
            encoded_image = base64.b64encode(image_bytes).decode("utf-8")

            client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=" ",
            )

            completion = client.chat.completions.create(
                extra_headers={
                    "HTTP-Referer": "<YOUR_SITE_URL>",
                    "X-Title": "<YOUR_SITE_NAME>",
                },
                extra_body={},
                model="qwen/qwen2.5-vl-32b-instruct:free",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": user_input
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{encoded_image}"  # Base64 formatında resmi gönder
                                }
                            }
                        ]
                    }
                ]
            )

            # Yanıtı kontrol et
            if completion.choices:
                st.write(completion.choices[0].message.content)
            else:
                st.write("Yanıt alınamadı.")

if __name__ == "__main__":
    main()