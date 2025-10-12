# Filename: W1205_GenAI_Similarity_05.py
# Visualization by drawing a similarity matrix heat map

# !pip install matplotlib seaborn scikit-learn

import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm
import datetime, time
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

# 中文文件
documents = [
    "這是第一份文件。",
    "這份文件是第二份文件。",
    "而這是第三份。",
    "這是第一份文件嗎？",
]

# 指定字型檔案路徑
font_path = "fonts/chinese_font.ttf"  # 修改為你的字型路徑

# 使用 jieba 做中文斷詞
def jieba_tokenizer(text):
    return jieba.lcut(text)

# 文件轉向量
def embed_documents(documents):
    vectorizer = TfidfVectorizer(tokenizer=jieba_tokenizer)
    vectorizer.fit(documents)
    embeddings = vectorizer.transform(documents).toarray()
    return embeddings

# 使用餘弦相似度公式計算文件相似性
def calculate_similarity(embeddings):
    return cosine_similarity(embeddings)

# 繪製相似度矩陣熱力圖
def plot_heatmap(similarities, labels):
    plt.figure(figsize=(8, 6))
    custom_font = fm.FontProperties(fname=font_path, size=12)  # 設定字型大小
    sns.heatmap(similarities, annot=True, cmap="YlGnBu", xticklabels=labels, yticklabels=labels)
    plt.title("文件間餘弦相似度熱力圖", fontproperties=custom_font)
    plt.xlabel("文件", fontproperties=custom_font)
    plt.ylabel("文件",fontproperties=custom_font)
    plt.tight_layout()
    plt.show()

def print_assignment_info(student_id):
    print("\n-----------------------------")
    print(f"W12 Assignment 5 | Student ID: {student_id} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-----------------------------\n")

# 主程式
def main():
    student_id = "YourStudentID1234"  # ← 請在這裡填上你的學號

    for i in tqdm(range(3), desc="處理中"):
        time.sleep(1)  # 模擬等待

    embeddings = embed_documents(documents)

    print("\n輸入文件：")
    for i, doc in enumerate(documents, 1):
        print(f"{i}: {doc}")

    similarities = calculate_similarity(embeddings)

    print("\n文件間餘弦相似度矩陣：")
    print(similarities)

    labels = [f"doc{i+1}" for i in range(len(documents))]
    plot_heatmap(similarities, labels)

    print_assignment_info(student_id)

if __name__ == "__main__":
    main()
