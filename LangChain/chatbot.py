import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")
load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

condition = True

while condition == True:
    question = input("Enter your Question : ")
    if question == "exit":
        break
    else:
        ans = model.invoke(question)
        print(ans.content)