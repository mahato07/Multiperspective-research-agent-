import os
from dotenv import load_dotenv
from langsmith import wrappers
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

try:
    llm = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash-lite",
        temperature=1.0)
    response = llm.invoke("which gemini model is this")
    print("check", response.content)

except Exception as e:
    print("api error", e)
