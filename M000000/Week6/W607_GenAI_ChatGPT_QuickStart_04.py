#Filename: W607_GenAI_ChatGPT_QuickStart_04.py
import datetime, os
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

completion = client.chat.completions.create(
    model="gpt-4o-audio-preview",
    modalities=["text", "audio"],
    audio={"voice": "alloy", "format": "mp3"},
    messages=[
        {
            "role": "user",
            "content": "Why is National Taiwan University of Science and Technology the best university in Taiwan? Could you give me a reason?"
        }
    ]
)

print(completion.choices[0])

# Ensure the 'audio/' directory exists before writing the file
output_dir = "audio"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

mp3_bytes = base64.b64decode(completion.choices[0].message.audio.data)
with open("audio/ntust.mp3", "wb") as f:
    f.write(mp3_bytes)

# Assignment setting: Please enter your Student ID.
print(" ")
print('W6 Assignment 4'+ ' | Student ID | ', datetime.datetime.now())
