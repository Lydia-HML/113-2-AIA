#filename: W704_GenAI_word_embeddings_04.py

## 2.4 Adding special context tokens
## Goal: We need to modify the tokenizer to handle unknown words.
## Apply this vocabulary to convert new text into token IDs

import datetime
import re
from W703_GenAI_word_embeddings_03 import SimpleTokenizerV1

# Define SimpleTokenizerV2
class SimpleTokenizerV2:
    def __init__(self, vocab):
        self.str_to_int = vocab
        self.int_to_str = {i: s for s, i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        preprocessed = [ # Replaces unknown words by <|unk|> tokens
            item if item in self.str_to_int
            else "<|unk|>" for item in preprocessed
        ]

        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text) # Replace spaces before the specified punctuations
        return text



# Read file content and split
with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# Step 1: Data Preprocess get the vocab
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
vocab = {token:integer for integer,token in enumerate(all_words)}

# Step 2: : Apply this vocabulary to convert new text into token IDs
tokenizer = SimpleTokenizerV1(vocab)
text = "Hello, do you like tea. Is this-- a test?"
# tokenizer.encode(text)   #Error, because unknown

print()
print("The number of vocabulary items: (Before)", len(vocab.items()))

#
all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])

vocab = {token:integer for integer,token in enumerate(all_tokens)}
print("The number of vocabulary items: (After)", len(vocab.items()))
print()

for i, item in enumerate(list(vocab.items())[-5:]):
    print("Last 5 vocabulary items:", item)

# Using SimpleTokenizerV2 to get the tokens
print()
print("-----SimpleTokenizerV2-----")
tokenizer = SimpleTokenizerV2(vocab)

text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."

text = " <|endoftext|> ".join((text1, text2))

print("text: ", text)

print("After Encoding: ", tokenizer.encode(text))
print("After Decoding: ",tokenizer.decode(tokenizer.encode(text)))

# Assignment setting: Please enter your Student ID.
print(" ")
print('W7 Assignment 4'+ ' | Student ID | ', datetime.datetime.now())


