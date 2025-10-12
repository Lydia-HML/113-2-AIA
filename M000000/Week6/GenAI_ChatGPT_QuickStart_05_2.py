#Filename: GenAI_ChatGPT_QuickStart_05_2.py
import datetime
import base64

from openai import OpenAI

#GenAI_W6 Key (Expired on 2025-03-17 13:00 Limited)
# your_openai_api_key = "sk-proj-your-key"
# client = OpenAI(api_key= your_openai_api_key )

import os
from dotenv import load_dotenv
load_dotenv(override=True)
client = OpenAI(api_key= os.getenv("OPENAI_API_KEY") )


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
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")



# Assignment setting: Please enter your Student ID.
print(" ")
print('W6 Assignment 5'+ ' | Student ID | ', datetime.datetime.now())
