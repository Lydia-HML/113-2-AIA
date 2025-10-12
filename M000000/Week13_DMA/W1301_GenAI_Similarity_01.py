# Filename: W1301_GenAI_Similarity_01.py

# !pip install transformers
# !pip install sentence_transformers
# !pip install torch
# !pip install openai
# !pip install langchain
# !pip install scikit-learn
# !pip install numpy
# !pip install tqdm

from transformers import BertTokenizer, BertModel
import torch
import numpy as np
from tqdm import tqdm
import time, datetime

# Example documents
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]

# Step 1: Tokenize and Embed Text (文字轉向量)
def embed_documents(documents):
    # Choose embedding model
    model_name = 'bert-base-uncased'
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertModel.from_pretrained(model_name)

    # Tokenize and embed each document
    embeddings = []
    for doc in documents:
        inputs = tokenizer(doc, return_tensors='pt', max_length=512, truncation=True)
        with torch.no_grad():
            outputs = model(**inputs)
        # Extract embeddings from the second-to-last layer
        embeddings.append(outputs.last_hidden_state.mean(dim=1).squeeze().numpy())
    return np.array(embeddings)


# Step 2: Utilize Embeddings and calculate similarity between documents (計算相似度)
def calculate_similarity(embeddings):
    similarities = np.inner(embeddings, embeddings)
    return similarities

def print_assignment_info(student_id):
    print("\n-----------------------------")
    print(f"W13 Assignment 1 | Student ID: {student_id} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-----------------------------\n")

def main():

    student_id = "YourStudentID1234"  # ← 請在這裡填上你的學號
    print_assignment_info(student_id)

    embeddings = embed_documents(documents)

    for i in tqdm(range(10), desc="Processing"):
        time.sleep(1)  # 模擬等待

    similarities = calculate_similarity(embeddings)
    print("Similarity Matrix:")
    print(similarities)


if __name__ == "__main__":
    main()