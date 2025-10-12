# 📘 使用圖形與向量資料庫查詢電影資料

作者：林筱玫  
日期：2025-05-06

---

## 🎯 教學目標

- 認識圖形資料庫 Neo4j 與其應用場景
- 使用 LangChain 串接圖形資料與向量資料庫
- 整合評論與結構化資料，回應自然語言問題
- 以模組化方式構建查詢流程，可重複與擴充
- 建立 AI 助理系統自動判斷使用何種查詢方式

---

## 📦 專案結構

```bash
langchain_ch08_refactor/
├── config.py               # 環境變數與模型初始化
├── graph_setup.py          # Neo4j 連接與資料匯入
├── vector_setup.py         # 建立向量資料庫
├── qa_chain.py             # 問答鏈建構
├── tools.py                # LangChain 工具封裝
├── agent_runner.py         # Agent 整合與提示詞設計
├── main.py                 # 主互動 CLI 執行程式
└── README.md               # 使用說明
```

---

## 🔧 第一步：設定環境（`config.py`）

```python
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv(override=True)
chat_model = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

---

## 🧠 第二步：匯入電影知識圖譜（`graph_setup.py`）

匯入 `movie_data.csv` 來建立包含演員、導演、類型的圖形結構：

```cypher
MERGE (m:Movie {id:row.MovieID})
MERGE (p:Person {name:...})-[:ACTED_IN]->(m)
MERGE (g:Genre {name:...})<-[:IN_GENRE]-(m)
```

建立好後使用：

```python
graph.refresh_schema()
```

---

## ✨ 第三步：建立向量資料庫（`vector_setup.py`）

使用評論資料建立向量索引：

```python
loader = CSVLoader('./movie.csv')
docs = loader.load()
Neo4jVector.from_documents(docs, embedding=...)
```

---

## 🔍 第四步：問答鏈建構（`qa_chain.py`）

### 圖形查詢鏈（Cypher QA）
```python
GraphCypherQAChain.from_llm(graph=graph, llm=chat_model)
```

### 向量查詢鏈
```python
retriever ➜ prompt ➜ chat_model ➜ output_parser
```

---

## 🛠 第五步：建立 LangChain 工具（`tools.py`）

```python
StructuredTool.from_function(func=vector_chain.invoke, name="Reviews", ...)
```

```python
StructuredTool.from_function(func=cypher_chain.invoke, name="Graph", ...)
```

---

## 🤖 第六步：整合 Agent（`agent_runner.py`）

使用 LangChain 代理架構，智慧選擇工具回答問題：

```python
create_openai_tools_agent(chat_model, tools, prompt_template)
```

---

## 💬 第七步：執行主程式（`main.py`）

```python
while True:
    msg = input("我說：")
    ...
```

---

## ✅ 建議練習

- 修改查詢語句，如查詢某導演的作品
- 將向量資料換成自訂影評
- 增加第三種工具，例如電影獎項查詢
- 將 CLI 版本改寫為網頁版本（可用 Streamlit）

---

