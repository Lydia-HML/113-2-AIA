# Filename: W1106_GenAI_LC_CalTokens_05.py
# Token 計算: 「問一題、問一組題目，並且順便記錄 token 消耗」的小實驗
import os
import datetime
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.callbacks import get_openai_callback
from rich import print as pprint

# 載入環境變數
load_dotenv(override=True)

def invoke_single_prompt(llm, prompt):
    with get_openai_callback() as cb:
        result = llm.invoke(prompt)
        print(f"Model [{llm.model}] - Total Tokens: {cb.total_tokens}")
        print(f"Result ID: {result.id}")
        pprint(cb)
    print(" ")

def batch_invoke_prompts(llm, prompts):
    llm.cache = False
    with get_openai_callback() as cb:
        results = llm.batch(prompts)
        for result in results:
            print(result.content)
        pprint(cb)
    print(" ")

def print_assignment_info(student_id):
    print("\n-----------------------------")
    print(f"W11 Assignment 6 | Student ID: {student_id} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-----------------------------\n")

def main():
    # 建立 LLM 物件
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)

    # 單句測試
    invoke_single_prompt(llm, "你好, 使用繁體中文")

    # 多句 batch 測試
    prompts = [
        "我家小狗叫 lucky, 使用繁體中文",
        "我家小狗叫什麼？, 使用繁體中文"
    ]
    batch_invoke_prompts(llm, prompts)

    # 作業標記
    student_id = "YourStudentID1234"  # ← 記得換成你的學號
    print_assignment_info(student_id)

# 若本程式被執行，視為程式的進入點，則執行 main()
if __name__ == "__main__":
    main()