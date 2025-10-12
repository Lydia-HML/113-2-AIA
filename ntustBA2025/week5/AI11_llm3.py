# streamlit run AI11_llm3.py
import streamlit as st
import ollama
import random

st.title("Gemma3 多模態 LLM 應用範例")
colors = ['red', 'blue', 'green', 'orange', 'purple']
user_input = st.text_input("詢問任何問題：", "")
uploaded_image = st.file_uploader("可同時上傳圖片（jpg/png）", type=["jpg", "jpeg", "png"])

if st.button("send"):
    if user_input or uploaded_image:
        st.markdown(f"<span style='color:{random.choice(colors)};'>請稍待片刻，思考中，馬上回答...</span>"
                ,unsafe_allow_html=True)
        messages = []
        if uploaded_image:
            st.image(uploaded_image, caption="上傳的圖片如上，請等待判讀結果...", use_container_width=True)
            image_bytes = uploaded_image.getvalue()
            messages.append({'role': 'user', 'content': user_input, 'images': [image_bytes]})
        else:
            messages.append({'role': 'user', 'content': user_input})
        response = ollama.chat(model='gemma3:latest', messages=messages)
        st.write(response['message']['content'])
    else:
        st.warning("請輸入prompt或上傳圖片！")