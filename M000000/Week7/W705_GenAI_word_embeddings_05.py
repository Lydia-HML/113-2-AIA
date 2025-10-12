#filename: W705_GenAI_word_embeddings_05.py
# !pip install tiktoken
# !pip install numpy

## 2.5 BytePair encoding
## The BPE tokenizer was used to train LLMs such as GPT-2, GPT-3, and the original model used in ChatGPT.
## Python open source library tiktoken (https://github.com/openai/tiktoken)

import datetime
import importlib
import tiktoken
from importlib.metadata import version
import torch

from torch.utils.data import Dataset, DataLoader

print("tiktoken version:", importlib.metadata.version("tiktoken"))
print("PyTorch version:", torch.__version__)
print()

# Instantiate the BPE tokenizer from tiktoken
tokenizer = tiktoken.get_encoding("gpt2")
text = (
    "Hello, do you like tea? <|endoftext|> In the sunlit terraces"
     "of someunknownPlace."
)
print("Input text:", text)

integers = tokenizer.encode(text, allowed_special={"<|endoftext|>"})
print("BPE-Encoding:", integers)

strings = tokenizer.decode(integers)
print("BPE-Decoding:", strings)

# Assignment setting: Please enter your Student ID.
print(" ")
print('W7 Assignment 5'+ ' | Student ID | ', datetime.datetime.now())
