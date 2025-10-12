#!pip install python-dotenv

from dotenv import load_dotenv
load_dotenv(override=True)

import os
import openai
# 預設匯入時就會從 OPENAI_API_KEY 環境變數讀取金鑰

openai.api_key = os.getenv('GEMINI_API_KEY')
print(os.getenv("GEMINI_API_KEY"))