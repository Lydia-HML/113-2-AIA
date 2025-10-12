# Filename: W1102_GenAI_LC_hello_01_openai.py
# 用 GPT-3.5-Turbo 回應一個中文問候，然後印出結果（好幾種不同方式）
#!pip install openai
#!pip install langchain
#!pip install -U langchain-community
#!pip install langchain_openai rich

from langchain_openai import ChatOpenAI
import openai
import os, datetime
from dotenv import load_dotenv
load_dotenv(override=True)

# 建立 OpenAI 物件
openai.api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model_name="gpt-3.5-turbo", api_key=openai.api_key)
response = llm.invoke("你好, 使用繁體中文")
print(response)

response.pretty_print()
#
from rich import print as pprint
pprint(response)

# Assignment setting: Please enter your Student ID.
print("\n-----------------------------")
student_id = "YourStudentID1234"  # ← 請在這裡填上你的學號
print(f"W11 Assignment 2-2 | Student ID: {student_id} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("-----------------------------\n")
