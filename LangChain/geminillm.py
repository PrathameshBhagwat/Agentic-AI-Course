import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI

load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")
load_dotenv()

model = GoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)

result = model.invoke("Who is the 2011 Cricket World Cup winning captain ?")

print(result)