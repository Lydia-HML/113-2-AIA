# Filename: W706_GenAI_word_embeddings_06.py

## 2.6 Data sampling with a sliding window
## A dataset for batched inputs and targets

import datetime
import tiktoken
import torch
from torch.utils.data import Dataset, DataLoader

class GPTDatasetV1(Dataset):
    def __init__(self, txt, tokenizer, max_length, stride):
        self.input_ids = []
        self.target_ids = []

        # Tokenize the entire text
        token_ids = tokenizer.encode(txt, allowed_special={"<|endoftext|>"})  # Tokenizes the entire text

        # Use a sliding window to chunk the book into overlapping sequences of max_length
        for i in range(0, len(token_ids) - max_length, stride):
            input_chunk = token_ids[i:i + max_length]
            target_chunk = token_ids[i + 1: i + max_length + 1]
            self.input_ids.append(torch.tensor(input_chunk))
            self.target_ids.append(torch.tensor(target_chunk))

    def __len__(self):  # Returns the total number of rows in the dataset
        return len(self.input_ids)

    def __getitem__(self, idx):  #Returns a single row from the dataset
        return self.input_ids[idx], self.target_ids[idx]


# A data loader to generate batches with input-with pairs
def create_dataloader_v1(txt, batch_size=4, max_length=256,
                         stride=128, shuffle=True, drop_last=True,
                         num_workers=0):

    # Initialize the tokenizer
    tokenizer = tiktoken.get_encoding("gpt2")

    # Create dataset
    dataset = GPTDatasetV1(txt, tokenizer, max_length, stride)

    # Create dataloader
    dataloader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        drop_last=drop_last,  # drop_last=True drops the last batch
                              # if it is shorter than the specified batch_size to prevent loss spikes during training.
        num_workers=num_workers
    )

    return dataloader

##################################################################################################################
# Read file content and use BPE tokenizer to split tokens
with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

tokenizer = tiktoken.get_encoding("gpt2")
print("raw_text:", len(raw_text))

enc_text = tokenizer.encode(raw_text)
print("enc_text:",len(enc_text)) # the total number of tokens in the training set, after applying the BPE tokenizer.

enc_sample = enc_text[50:]
print("enc_sample: ",enc_sample)

##################################################################################################################
# Exercise 1: token ID
# One of the easiest and most intuitive ways to create the input–target pairs for the next-word prediction task
# is to create two variables, x and y, where x contains the input tokens and y contains the targets,
# which are the inputs shifted by 1:
##################################################################################################################
context_size = 4  # The context size determines how many tokens are included in the input.
x = enc_sample[:context_size]
y = enc_sample[1:context_size+1]

print(f"x: {x}")
print(f"y:      {y}")

# token ID
for i in range(1, context_size+1):
    context = enc_sample[:i]
    desired = enc_sample[i]

    print(context, "---->", desired)
    # Everything left of the arrow (---->) refers to the input an LLM would receive.
    # The token ID on the right side of the arrow represents the target token ID that the LLM is supposed to predict.

# convert the token IDs into text
for i in range(1, context_size+1):
    context = enc_sample[:i]
    desired = enc_sample[i]

    print(tokenizer.decode(context), "---->", tokenizer.decode([desired])) #input and outputs look in text format

##################################################################################################################
# Exercise 2: token ID
# Implementing an efficient data loader that iterates over the input dataset and
# returns the inputs and targets as PyTorch tensors.
##################################################################################################################
dataloader = create_dataloader_v1(
    raw_text, batch_size=1, max_length=4, stride=1, shuffle=False
)

data_iter = iter(dataloader) # Converts dataloader into a Python iterator
first_batch = next(data_iter) # Fetch the next entry via Python’s built-in next() function
print("first_batch: ", first_batch)

second_batch = next(data_iter)
print("second_batch: ", second_batch)

dataloader = create_dataloader_v1(raw_text, batch_size=8, max_length=4, stride=1, shuffle=False)

data_iter = iter(dataloader)
inputs, targets = next(data_iter)
print("Inputs:\n", inputs)
print("\nTargets:\n", targets)

inputs2, targets2 = next(data_iter)
print("Inputs2:\n", inputs2)
print("\nTargets2:\n", targets2)


# Assignment setting: Please enter your Student ID.
print(" ")
print('W7 Assignment 6'+ ' | Student ID | ', datetime.datetime.now())


