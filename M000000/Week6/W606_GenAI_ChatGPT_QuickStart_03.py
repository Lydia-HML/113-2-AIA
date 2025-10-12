#Filename: W606_GenAI_ChatGPT_QuickStart_03.py
import datetime

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

response = client.images.generate(
    model="dall-e-3",
    prompt="a white siamese cat",
    size="1024x1024",
    quality="standard",
    n=1,
)

print(response.data[0].url)

# Assignment setting: Please enter your Student ID.
print(" ")
print('W6 Assignment 3'+ ' | Student ID | ', datetime.datetime.now())
