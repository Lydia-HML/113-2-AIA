#Filename: GenAI_ChatGPT_QuickStart_01.py
import datetime
import os
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv(override=True)


# Provide your OpenAI API key here
load_dotenv(override=True)

client = OpenAI(api_key= os.getenv("OPENAI_API_KEY") )

completion = client.chat.completions.create(
    model='gpt-4o',
    messages=[
        dict(role="user", content="Write a one-sentence bedtime story about a unicorn."),
    ]
)


print("Story: " + completion.choices[0].message.content)

# Assignment setting: Please enter your Student ID.
print(" ")
print('W6 Assignment 1'+ ' | M000000 | ', datetime.datetime.now())
