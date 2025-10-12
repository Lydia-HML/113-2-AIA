#Filename: W605_GenAI_ChatGPT_QuickStart_02.py
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

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                    },
                },
            ],
        }
    ],
)

print(response.choices[0].message.content)

# Assignment setting: Please enter your Student ID.
print(" ")
print('W6 Assignment 2'+ ' | Student ID | ', datetime.datetime.now())
