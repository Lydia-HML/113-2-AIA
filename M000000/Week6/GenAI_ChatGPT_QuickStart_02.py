#Filename: GenAI_ChatGPT_QuickStart_02.py
import datetime

from openai import OpenAI

#GenAI_W6 Key (Expired on 2025-03-17 13:00 Limited)
# your_openai_api_key = "sk-proj-your-key"
#
# client = OpenAI(api_key= your_openai_api_key )
import os
from dotenv import load_dotenv
load_dotenv(override=True)
client = OpenAI(api_key= os.getenv("OPENAI_API_KEY") )


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
