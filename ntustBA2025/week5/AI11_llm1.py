# streamlit run AI11_llm1.py
import streamlit as st
import ollama
import random

st.title("Gemma3 純文字 LLM 應用範例")
colors = ['red', 'blue', 'green', 'orange', 'purple']
user_input = st.text_input("詢問任何問題：", "")

if st.button("send") or user_input:
    st.markdown(f"<span style='color:{random.choice(colors)};'>請稍待片刻，思考中，馬上回答...</span>",
                unsafe_allow_html=True)
    # response = ollama.chat(model='gemma3:1b', messages=[{'role': 'user', 'content': user_input}])
    response = ollama.chat(model='llama3.2:1b', messages=[{'role': 'user', 'content': user_input}])
    st.write(response['message']['content'])
else:
    st.warning("Please type in your question!")