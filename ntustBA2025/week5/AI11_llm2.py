# streamlit run AI11_llm2.py
import streamlit as st
import ollama
from gtts.lang import tts_langs
from gtts import gTTS
import base64
from tempfile import NamedTemporaryFile

langs = tts_langs().keys()
st.title("Gemma3 文字語音LLM TTS應用範例")
lang = st.selectbox("Please choose the language", options=langs, index=12) # en 12
user_input = st.text_area("詢問任何問題：", "")

if st.button("send"):
    if user_input:
        st.markdown(f"<span style='color:red;'>請稍待片刻，gemma3:1b思考中...</span>",unsafe_allow_html=True)
        response = ollama.chat(model='gemma3:1b', messages=[{'role': 'user', 'content': user_input}])
        st.write(response['message']['content'])
        tts = gTTS(response['message']['content'], lang=lang, slow=False, lang_check=True)
        with NamedTemporaryFile(suffix=".mp3", delete=False) as temp:
            tts.save(temp.name)
            with open(temp.name, "rb") as f:
                data = f.read()
                b64 = base64.b64encode(data).decode()
                md = f"""<audio controls autoplay="true">
                     <source src="data:audio/mp3;base64,{b64}" type = "audio/mp3">
                     your browser does not support the audio element. </audio>"""
                st.markdown(md, unsafe_allow_html=True,)
    else:
        st.warning("PLease type in your question!")