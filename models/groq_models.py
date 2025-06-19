from langchain_groq import ChatGroq
import os

groq_api = os.getenv("GROQ_API_KEY")
model = os.getenv("GROQ_MODEL", "llama3-70b-8192")

groq_model = ChatGroq(
    model=model,
    temperature=0.3,
    api_key=groq_api
)