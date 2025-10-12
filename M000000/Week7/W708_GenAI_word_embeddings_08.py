# Filename: W708_GenAI_word_embeddings_08.py

## 2.8 Encoding word positions

import datetime
import torch
from W706_GenAI_word_embeddings_06 import create_dataloader_v1

##################################################################################################################
# let’s consider more realistic and useful embedding sizes and encode the input tokens into a
# 256-dimensional vector representation, which is smaller than what the original GPT-3 model used
# (in GPT-3, the embedding size is 12,288 dimensions) but still reasonable for experimentation.
# Furthermore, we assume that the token IDs were created by the BPE tokenizer we implemented earlier,
# which has a vocabulary size of 50,257
##################################################################################################################


vocab_size = 50257
output_dim = 256

token_embedding_layer = torch.nn.Embedding(vocab_size, output_dim)


# Read file content and split
with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# Using the previous token_embedding_layer, if we sample data from the data loader, we embed each token
# in each batch into a 256-dimensional vector. If we have a batch size of 8 with four tokens each,
# the result will be an 8 × 4 × 256 tensor.
max_length = 4
dataloader = create_dataloader_v1(
    raw_text, batch_size=8, max_length=max_length,
    stride=max_length, shuffle=False
)
data_iter = iter(dataloader)
inputs, targets = next(data_iter)

print("Token IDs:\n", inputs)
print("\nInputs shape:\n", inputs.shape)

token_embeddings = token_embedding_layer(inputs)
print("\nToken_embeddings.shape:\n", token_embeddings.shape)

# Let’s now use the embedding layer to embed these token IDs into 256-dimensional vectors
context_length = max_length
pos_embedding_layer = torch.nn.Embedding(context_length, output_dim)
pos_embeddings = pos_embedding_layer(torch.arange(max_length))
print("\nPositional_embeddings.shape:\n ", pos_embeddings.shape)

# uncomment & execute the following line to see how the embeddings look like
# print(pos_embeddings)

input_embeddings = token_embeddings + pos_embeddings
print("\nInput_embeddings.shape:\n", input_embeddings.shape)

# uncomment & execute the following line to see how the embeddings look like
# print(input_embeddings)

# Assignment setting: Please enter your Student ID.
print(" ")
print('W7 Assignment 8'+ ' | Student ID | ', datetime.datetime.now())