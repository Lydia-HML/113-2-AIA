#filename: W701_GenAI_word_embeddings_01.py
# !pip install torch
# !pip install tiktoken

from importlib.metadata import version
import os
import urllib.request
import datetime

print("torch version:", version("torch"))
print("tiktoken version:", version("tiktoken"))

if not os.path.exists("the-verdict.txt"):
    url = ("https://raw.githubusercontent.com/rasbt/"
           "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
           "the-verdict.txt")
    file_path = "the-verdict.txt"
    urllib.request.urlretrieve(url, file_path)

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

print("Total number of character:", len(raw_text))

# Read the first 100 characters of the article
print(raw_text[:99])

# Assignment setting: Please enter your Student ID.
print(" ")
print('W7 Assignment 1'+ ' | Student ID | ', datetime.datetime.now())