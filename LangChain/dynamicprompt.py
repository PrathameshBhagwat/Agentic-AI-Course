import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

topic = input("Enter your topic: ")

prompt = f"Explain {topic} in simple language with an example."

res = model.invoke(prompt)

print(res.content)