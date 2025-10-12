# Filename: W1304_GenAI_Similarity_04.py

# Change the similarity calculation from inner product (np.inner) to the standard cosine similarity
# formula function : sklearn.metrics.pairwise.cosine_similarity()

import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm
import datetime, time

# 中文語料集（corpus）
documents = [
    "這是第一份文件。",
    "這份文件是第二份文件。",
    "而這是第三份。",
    "這是第一份文件嗎？",
]

# 使用 jieba 做中文斷詞
def jieba_tokenizer(text):
    return jieba.lcut(text)

# 文件轉向量
def embed_documents(documents):
    vectorizer = TfidfVectorizer(tokenizer=jieba_tokenizer) #建立 TF-IDF 向量模型：將詞彙在各文件中的重要性編碼成向量。
    vectorizer.fit(documents) #建立詞彙表。
    embeddings = vectorizer.transform(documents).toarray()  #.transform()：將每份文件轉為向量（稀疏矩陣，轉成陣列）。
    return embeddings

# 使用餘弦相似度（cosine similarity）公式, 衡量向量間角度, 計算文件相似性 。
def calculate_similarity(embeddings):
    return cosine_similarity(embeddings) #數值介於 [0, 1]，越接近 1 表示越相似。

def print_assignment_info(student_id):
    print("\n-----------------------------")
    print(f"W13 Assignment 4 | Student ID: {student_id} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-----------------------------\n")

# 主程式
def main():
    student_id = "YourStudentID1234"  # ← 請在這裡填上你的學號
    print_assignment_info(student_id)

    for i in tqdm(range(5), desc="處理中"):
        time.sleep(1)  # 模擬等待

    embeddings = embed_documents(documents)

    print("\n輸入文件：")
    for i, doc in enumerate(documents, 1):
        print(f"{i}: {doc}")

    similarities = calculate_similarity(embeddings)

    print("\n文件間餘弦相似度矩陣：")
    print(similarities)

if __name__ == "__main__":
    main()
