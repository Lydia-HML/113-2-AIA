# Filename: W1308_GenAI_LC_RAG_08_streamlit.py
# ========================
# LangChain RAG + Streamlit GUI 介面
# ========================

#!pip install pypdf chromadb streamlit

import os
import datetime
from dotenv import load_dotenv
import openai
import streamlit as st

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (RecursiveCharacterTextSplitter)
from langchain_chroma import Chroma
from langchain.schema import HumanMessage

def init_environment():
    load_dotenv(override=True)
    os.environ["USER_AGENT"] = "LangChain-RAG-Agent/1.0"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    return openai.api_key, os.getenv("GEMINI_API_KEY")

def init_llms(openai_key):
    openai_llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_key)
    gemini_llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)
    return openai_llm, gemini_llm

def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

# 使用 LangChain 的 PyPDFLoader 將 PDF 解析成文本。
# 使用 RecursiveCharacterTextSplitter 拆分成可嵌入（embedding）的 chunks。
def load_and_split_pdf(pdf_path, chunk_size=500, chunk_overlap=20):
    loader = PyPDFLoader(file_path=pdf_path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return docs, splitter.split_documents(docs)

#把 chunks 轉成向量並存入本地 ./chroma_langchain_db 中，可被用於檢索式問答（RAG）。
def create_chroma_db(chunks, embedding_model, db_path):
    return Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=db_path,
        collection_metadata={"hnsw:space": "cosine"}
    )

# 使用 Retriever 找出與問題最相關的內容。
# 用 prompt 模板將上下文與問題包裝給 LLM 回答。
def retrieve_and_ask(llm, retriever, query):
    docs = retriever.invoke(query)
    context = "\n".join([doc.page_content for doc in docs if hasattr(doc, "page_content")])
    prompt = f"請根據以下內容回答問題:\n\n{context}\n\n問題: {query}"
    return llm.invoke([HumanMessage(content=prompt)]), context

def save_output(question, context, answer, output_path="./output"):
    ensure_directory(output_path)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(output_path, f"rag_result_{timestamp}.txt")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("[Query]\n" + question + "\n\n")
        f.write("[Retrieved Context]\n" + context + "\n\n")
        f.write("[Answer]\n" + answer + "\n")
    return filename

def print_assignment_info(student_id):
    print("\n-----------------------------")
    print(f"W13 Assignment 8 | Student ID: {student_id} | {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-----------------------------\n")


def main():
    student_id = "YourStudentID1234"  # ← 請在這裡填上你的學號

    st.set_page_config(page_title="🚦 Car Law RAG QA System", layout="wide")
    st.title("🚦 車輛法規 RAG 問答系統")
    st.markdown("輸入與車輛法規相關的問題，系統將從 PDF 檔案中找出資料並回答。")

    openai_key, _ = init_environment()
    openai_llm, _ = init_llms(openai_key)

    db_path = "./chroma_langchain_db"
    ensure_directory(db_path)

    uploaded_file = st.file_uploader("📄 上傳您要查詢的 PDF 法規文件：", type="pdf")

    if uploaded_file:
        with st.spinner("載入法規資料中..."):
            with open("./temp_uploaded.pdf", "wb") as f:
                f.write(uploaded_file.getbuffer())
            docs, chunks = load_and_split_pdf('./temp_uploaded.pdf')
            embeddings = OpenAIEmbeddings(model='text-embedding-3-large')
            db = create_chroma_db(chunks, embeddings, db_path)
            retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 6})

        query = st.text_area("請輸入您的問題（繁體中文）:", "酒後開車且酒精濃度超過規定標準應罰款多少?", height=100)

        if st.button("🚀 查詢"):
            with st.spinner("正在查詢中..."):
                response, context = retrieve_and_ask(openai_llm, retriever, query)
                st.success("✅ 回答完成！")
                st.subheader("🔹 回答內容")
                st.write(response.content)

                with st.expander("🔍 檢索內容（Context）"):
                    st.code(context)

                filename = save_output(query, context, response.content)
                st.download_button("💾 下載結果檔案", data=open(filename, "r", encoding="utf-8").read(), file_name=os.path.basename(filename))
    else:
        st.warning("請先上傳一份 PDF 文件以啟動查詢功能。")

    print_assignment_info(student_id)

if __name__ == "__main__":
    main()
