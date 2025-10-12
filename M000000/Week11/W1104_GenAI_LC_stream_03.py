# Filename: W1104_GenAI_LC_stream_03.py
# Stream

import os
import datetime
from dotenv import load_dotenv
from rich import print as pprint
from langchain_google_genai import ChatGoogleGenerativeAI

# 載入環境變數
load_dotenv(override=True)

def stream_and_print(llm, prompt, separator="", show_object=False):
    chunks = []
    for chunk in llm.stream(prompt):
        chunks.append(chunk)
        output = chunk if show_object else chunk.content
        pprint(output, end=separator, flush=True)
    print("\n")  # 確保每個輸出結束後換行
    return chunks

def print_assignment_info(student_id):
    print("\n-----------------------------")
    print(f"W11 Assignment 4 | Student ID: {student_id} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-----------------------------\n")

def main():
    # 建立 LLM 物件
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",  # 使用 Gemini 2.0 Flash 版本
        temperature=0.7,  # 生成內容的隨機程度 (0~1)，0.7 為中度創意
    )

    # stream exercise 1 : 對給定的 Prompt 使用 stream() 方法，讓 AI 回傳內容。
    print("exercise 1-1: show_object=True 把回傳的整個 chunk 物件印出來")
    stream_and_print(llm, "你好, 使用繁體中文", show_object=True)
    print("exercise 1-2: show_object=False 只印出chunk 的內容（也就是文字部分）")
    stream_and_print(llm, "你好, 使用繁體中文", show_object=False)

    # stream exercise 2
    print("exercise 2: show_object=True")
    stream_and_print(llm, "what color is the sky?", separator="|")

    # 作業標記
    student_id = "YourStudentID1234"  # ← 記得換成你的學號
    print_assignment_info(student_id)

# 若本程式被執行，視為程式的進入點，則執行 main()
if __name__ == "__main__":
    main()

