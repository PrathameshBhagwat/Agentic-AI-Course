import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)

country = input("Enter Country: ")

prompt = PromptTemplate(
    template="Whos is the PM of {country} ?",
    input_variables=["country"]
)

complete_prompt = prompt.invoke({"country":country})

ans = model.invoke(complete_prompt)

print(ans.content[0]["text"])