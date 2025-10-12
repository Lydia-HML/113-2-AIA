#Filename: GenAI_ChatGPT_QuickStart_03.py
import datetime

from openai import OpenAI

# #GenAI_W6 Key (Expired on 2025-03-17 13:00 Limited)
# your_openai_api_key = "sk-proj-your-key"
# client = OpenAI(api_key= your_openai_api_key )

import os
from dotenv import load_dotenv
load_dotenv(override=True)
client = OpenAI(api_key= os.getenv("OPENAI_API_KEY") )


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
