# Filename: W1207_GenAI_LC_toolcalling_07_gemini.py
# Tool creation, Tool binding, and Tool calling
import os, datetime
from dotenv import load_dotenv
load_dotenv(override=True)

from rich import print as pprint
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool


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
    print(f"W12 Assignment 7-1 | Student ID: {student_id} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-----------------------------\n")



def main():
    student_id = "YourStudentID1234"  # ← 請在這裡填上你的學號

    # 建立 Gemini LLM 物件
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)

    # use the tool directly
    print (multiply.invoke({"a": 2, "b": 3}))
    print (multiply.name)  # multiply schema
    print (multiply.description)  # Multiply two numbers.
    print (multiply.args)
    print ("\n")

    model = llm
    # Tool creation
    tools = [multiply, add]
    # Tool binding
    llm_with_tools = model.bind_tools(tools)
    # Tool calling


    result = llm_with_tools.invoke("Hello world!")
    pprint(result)
    result = llm_with_tools.invoke("What is 2 multiplied by 3?")
    pprint(result)
    result = llm_with_tools.invoke("What is 2 add by 3?")
    pprint(result)

    print_assignment_info(student_id)



# Run the async function in an asyncio event loop
if __name__ == "__main__":
    main()