#Filename: W608_GenAI_ChatGPT_QuickStart_05.py
import datetime
import base64

from openai import OpenAI

import os
import openai

from dotenv import load_dotenv
load_dotenv(override=True)

#GenAI_W6 Key (Expired on 2025-03-25 13:00 Limited)
#openai.api_key = "sk-proj-your-key"

# 預設匯入時就會從 OPENAI_API_KEY 環境變數讀取金鑰
openai.api_key = os.getenv('OPENAI_API_KEY')

# Provide your OpenAI API key here
client = OpenAI(api_key= openai.api_key )


stream = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "Say 'double bubble bath' ten times fast.",
        },
    ],
    stream=True,
)

for chunk in stream:
    print(chunk)
    print(chunk.choices[0].delta)
    print("****************")



# Assignment setting: Please enter your Student ID.
print(" ")
print('W6 Assignment 5'+ ' | Student ID | ', datetime.datetime.now())
