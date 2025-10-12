#filename: W702_GenAI_word_embeddings_02.py
import re  # regular expression
import datetime

text = "Hello, world. This, is a test."
result = re.split(r'(\s)', text)
print(result)

result = re.split(r'([,.]|\s)', text)
print(result)

# Strip whitespace from each item and then filter out any empty strings.
result = [item for item in result if item.strip()]
print(result)

text = "Hello, world. Is this-- a test?"

result = re.split(r'([,.:;?_!"()\']|--|\s)', text)
result = [item.strip() for item in result if item.strip()]
print(result)

# Read file content and split
with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(preprocessed[:30])

print(len(preprocessed))

# Assignment setting: Please enter your Student ID.
print(" ")
print('W7 Assignment 2'+ ' | Student ID | ', datetime.datetime.now())
