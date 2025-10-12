# Filename: W1206_GenAI_LC_prompts_06.py
# Token 計算
import asyncio
import datetime
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


# === 初始化 ===
def init_llms():
    load_dotenv(override=True)  # 若有使用 .env 金鑰
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)

    # 建立 prompt 與處理鏈
    prompt = ChatPromptTemplate.from_template("tell me a joke about {topic}")
    parser = StrOutputParser()
    chain = prompt | llm | parser
    return chain

# === 非同步執行函式 ===
async def generate_response(chain, topic="parrot"):
    print(f"\nGemini is generating a joke about: {topic}")
    async for chunk in chain.astream({"topic": topic}):
        print(chunk, end="|", flush=True)
    print("\n")

def print_assignment_info(student_id):
    print("\n-----------------------------")
    print(f"W12 Assignment 06 | Student ID: {student_id} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-----------------------------")

# === 主程式 ===
def main():

    student_id = "YourStudentID1234"  # ← 請在這裡填上你的學號
    print_assignment_info(student_id)

    chain = init_llms()
    asyncio.run(generate_response(chain))


# === 程式入口 ===
if __name__ == "__main__":
    main()
