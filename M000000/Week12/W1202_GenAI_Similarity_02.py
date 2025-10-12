# Filename: W1202_GenAI_Similarity_02.py

# 這個範例展示一個簡單的文字文件相似度分析工具，使用 TF-IDF 向量化技術與餘弦內積計算文件之間的相似性。

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from tqdm import tqdm
import time, datetime

# Example documents : 這是一組簡單英文句子，用來模擬小型文檔集（corpus）。
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?",
]

# Step 1: Using TF-IDF（Term Frequency-Inverse Document Frequency）to tokenize and embed text
# 向量化文本：TF-IDF
def embed_documents(documents):
    vectorizer = TfidfVectorizer() # Create a single TF-IDF vectorizer
    vectorizer.fit(documents) # Training：Create a consistent vocabulary
    embeddings = vectorizer.transform(documents).toarray()  # Transform each doc into a vector embedding
    return embeddings

# Step 2: Utilize embeddings and calculate similarity between documents
# 向量內積用來衡量文件間的相似度。
# 若使用的是 TF-IDF 向量，內積常可近似於餘弦相似度（若向量已正規化）。
def calculate_similarity(embeddings):
    similarities = np.inner(embeddings, embeddings)  # Inner product represents similarity
    return similarities

def print_assignment_info(student_id):
    print("\n-----------------------------")
    print(f"W12 Assignment 2 | Student ID: {student_id} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-----------------------------\n")

def main():

    student_id = "YourStudentID1234"  # ← 請在這裡填上你的學號


    for i in tqdm(range(10), desc="Processing"):
        time.sleep(1)  # 模擬等待

    embeddings = embed_documents(documents)
    print("Input Documents: \n[")
    for docs in documents:
        print (docs)
    print("]\n")

    similarities = calculate_similarity(embeddings)
    # 顯示相似度矩陣，通常是4x4對稱矩陣，對角線為1（自己與自己的相似度）。
    print("Similarity Matrix:")
    print(similarities)
    print_assignment_info(student_id)

if __name__ == "__main__":
    main()