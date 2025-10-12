#Filename: GenAI_ChatGPT_QuickStart_04.py
import datetime, os
import base64

from openai import OpenAI

#GenAI_W6 Key (Expired on 2025-03-17 13:00 Limited)
# your_openai_api_key = "sk-proj-your-key"
# client = OpenAI(api_key= your_openai_api_key )

import os
from dotenv import load_dotenv
load_dotenv(override=True)
client = OpenAI(api_key= os.getenv("OPENAI_API_KEY") )


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

wav_bytes = base64.b64decode(completion.choices[0].message.audio.data)
with open("audio/ntust.mp3", "wb") as f:
    f.write(wav_bytes)

# Assignment setting: Please enter your Student ID.
print(" ")
print('W6 Assignment 4'+ ' | Student ID | ', datetime.datetime.now())
