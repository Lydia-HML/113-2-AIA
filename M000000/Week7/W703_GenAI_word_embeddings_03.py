#filename: W703_GenAI_word_embeddings_03.py
import re
import datetime

## 2.3 Converting tokens into token IDs

#
class SimpleTokenizerV1:
    def __init__(self, vocab):
        self.str_to_int = vocab #Stores the vocabulary as a class attribute for access in the encode and decode methods0
        self.int_to_str = {i: s for s, i in vocab.items()} #Creates an inverse vocabulary that maps token IDs back to the original text tokens

    # Processes input text into token IDs
    def encode(self, text):
        preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)

        preprocessed = [
            item.strip() for item in preprocessed if item.strip()
        ]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    #Converts token IDs back into text
    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        # Replace spaces before the specified punctuations
        text = re.sub(r'\s+([,.?!"()\'])', r'\1', text) #Removes spaces before the specified punctuation
        return text

# Read file content and split
with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print("First 30 elements: ", preprocessed[:30])

all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
print("Vocabulary size: ", vocab_size)

vocab = {token:integer for integer,token in enumerate(all_words)}

# Create the vocabulary and print its first 51 entries
for i, item in enumerate(vocab.items()):
    print(item)
    if i >= 50:
        break

# Initial a Tokenizer by vocabulary
tokenizer = SimpleTokenizerV1(vocab)

text = """"It's the last he painted, you know," 
           Mrs. Gisburn said with pardonable pride."""
ids = tokenizer.encode(text)
print("Text to IDs: ", ids)

# Decode
print("IDs to Text: ", tokenizer.decode(ids))
#Encode then decode
print("Text to IDs to Text: ", tokenizer.decode(tokenizer.encode(text)))

# Assignment setting: Please enter your Student ID.
print(" ")
print('W7 Assignment 3'+ ' | Student ID | ', datetime.datetime.now())