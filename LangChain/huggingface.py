import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")
load_dotenv()

model = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

chatModel = ChatHuggingFace(llm=model)

response = chatModel.invoke(input("Enter the your question : "))

print(response.content)