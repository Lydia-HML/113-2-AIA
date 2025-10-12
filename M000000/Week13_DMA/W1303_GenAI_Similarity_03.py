# Filename: W1303_GenAI_Similarity_03.py
# !pip install jieba tqdm scikit-learn
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from tqdm import tqdm
import datetime, time

# 中文文件
documents = [
    "這是第一份文件。",
    "這份文件是第二份文件。",
    "而這是第三份。",
    "這是第一份文件嗎？",
]

# Step1: Use jieba to segment Chinese words 中文斷詞
# 使用 jieba 套件將一句中文分成詞語清單，例如：jieba.lcut("這是第一份文件") → ['這', '是', '第一份', '文件']
def jieba_tokenizer(text):
    return jieba.lcut(text)

# Step2: Convert the file to vector (文本向量化)
def embed_documents(documents):
    # 中文需要自己處理分詞，這裡用 jieba + TfidfVectorizer 的 tokenizer 參數
    vectorizer = TfidfVectorizer(tokenizer=jieba_tokenizer)
    vectorizer.fit(documents)
    embeddings = vectorizer.transform(documents).toarray()
    return embeddings

# Step3: Calculate file similarity (inner product)
def calculate_similarity(embeddings):
    similarities = np.inner(embeddings, embeddings)
    return similarities

def print_assignment_info(student_id):
    print("\n-----------------------------")
    print(f"W13 Assignment 3 | Student ID: {student_id} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-----------------------------\n")

# main
def main():
    student_id = "YourStudentID1234"  # ← 請在這裡填上你的學號
    print_assignment_info(student_id)

    for i in tqdm(range(5), desc="處理中"):
        time.sleep(1)  # Simulate waiting

    embeddings = embed_documents(documents)

    print("\n輸入文件：")
    for i, doc in enumerate(documents, 1):
        print(f"{i}: {doc}")

    similarities = calculate_similarity(embeddings)

    print("\n相似度矩陣：")
    print(similarities)

if __name__ == "__main__":
    main()
