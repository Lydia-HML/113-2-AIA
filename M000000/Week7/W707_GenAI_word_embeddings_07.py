#Filename: W707_GenAI_word_embeddings_07.py

## 2.7 Creating token embeddings

import torch
import datetime


input_ids = torch.tensor([2, 3, 5, 1])

vocab_size = 6
output_dim = 3

torch.manual_seed(123)
embedding_layer = torch.nn.Embedding(vocab_size, output_dim)

print(embedding_layer.weight)

print(embedding_layer(torch.tensor([3])))

print(embedding_layer(input_ids))

# Assignment setting: Please enter your Student ID.
print(" ")
print('W7 Assignment 7'+ ' | Student ID | ', datetime.datetime.now())
