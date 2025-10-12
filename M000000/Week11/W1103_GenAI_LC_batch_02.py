# Filename: W1103_GenAI_LC_batch_02.py
# Multiple messages by batch
import os, datetime
from dotenv import load_dotenv
load_dotenv(override=True)

from langchain_openai import ChatOpenAI
import openai
from rich import print as pprint
from langchain_google_genai import ChatGoogleGenerativeAI

# 建立 Gemini LLM 物件
llm = ChatGoogleGenerativeAI( model="gemini-2.0-flash", temperature=0.7)


# 多筆訊息
pprint(llm.batch(["我家小狗叫 lucky, 使用繁體中文",
                         "我家小狗叫什麼？, 使用繁體中文"]))

# Assignment setting: Please enter your Student ID.
print("\n-----------------------------")
student_id = "YourStudentID1234"  # ← 請在這裡填上你的學號
print(f"W11 Assignment 3 | Student ID: {student_id} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("-----------------------------\n")