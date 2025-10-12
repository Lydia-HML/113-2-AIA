# Filename: W1201_GenAI_LC_checkenv.py
# 同時建立兩種大語言模型（Gemini + OpenAI GPT），測試連線與基本問答功能
# !pip install langchain langchain_google_genai openai
# !pip install python-dotenv
# !pip install -U langchain-openai

from dotenv import load_dotenv
load_dotenv(override=True)
import os, datetime
from langchain_google_genai import ChatGoogleGenerativeAI
import openai
from langchain.chat_models import init_chat_model



#預設匯入時就會從 OPENAI_API_KEY 環境變數讀取金鑰
gemini_key = os.getenv('GEMINI_API_KEY')
print(f'\nGemini_API_KEY={gemini_key} \nGoogle Gemini API Key is ready!!!')
# 建立 Gemini LLM 物件
llm = ChatGoogleGenerativeAI( model="gemini-2.0-flash", temperature=0.7)
print(llm)
print("\nLangchain Framework for Gemini is ready,too :-) ")


#預設匯入時就會從 OPENAI_API_KEY 環境變數讀取金鑰
openai.api_key = os.getenv('OPENAI_API_KEY')
print(f'\nOPENAI_API_KEY={openai.api_key} \nOPENAI_API_KEY is ready!')
#建立 OpenAI 物件
llm = init_chat_model("gpt-3.5-turbo", model_provider="openai")
response = llm.invoke("Hello, Langchain world!")
print(response)
print("\nLangchain Framework for OpenAI is ready,too :-) ")

# Assignment setting: Please enter your Student ID.
print("\n-----------------------------")
student_id = "YourStudentID1234"  # ← 請在這裡填上你的學號
print(f"W12 Assignment 1 | Student ID: {student_id} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("-----------------------------\n")





