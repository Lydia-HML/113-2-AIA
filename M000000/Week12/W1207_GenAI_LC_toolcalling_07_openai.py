# Filename: W1207_GenAI_LC_toolcalling_07_openai.py
# Tool creation, Tool binding, and Tool calling
import os, datetime
from dotenv import load_dotenv
from pandas.io.formats.printing import pprint_thing

load_dotenv(override=True)
import asyncio  # Import asyncio to handle the async function

from rich import print as pprint
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
import openai
import os, datetime
from dotenv import load_dotenv

load_dotenv(override=True)


@tool
def multiply(a: int, b: int) -> int:
    """Multiply a and b."""
    return a * b
@tool
def add(a: int, b: int) -> int:
    """add a and b."""
    return a+b

def print_assignment_info(student_id):
    print("\n-----------------------------")
    print(f"W12 Assignment 7-2 | Student ID: {student_id} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-----------------------------\n")


def main():
    student_id = "YourStudentID1234"  # ← 請在這裡填上你的學號

    # 建立 Gemini LLM 物件

    # 建立 OpenAI 物件
    openai.api_key = os.getenv("OPENAI_API_KEY")
    llm = ChatOpenAI(model_name="gpt-4o", api_key=openai.api_key)
    response = llm.invoke("你好, 使用繁體中文")
    print(response)

    # use the tool directly
    print(multiply.invoke({"a": 2, "b": 3}))
    print(multiply.name)  # multiply schema
    print(multiply.description)  # Multiply two numbers.
    print(multiply.args)
    print("\n")

    model = llm
    # Tool creation
    tools = [multiply, add]
    # Tool binding
    llm_with_tools = model.bind_tools(tools)
    # Tool calling


    result = llm_with_tools.invoke("Hello world!")
    pprint(result)
    result = llm_with_tools.invoke("What is 2 multiplied by 3? give me the answer")
    pprint(result)
    result = llm_with_tools.invoke("What is 2 add by 3? give me the answer")
    pprint(result)

    print_assignment_info(student_id)

# Run the async function in an asyncio event loop
if __name__ == "__main__":
    main()
