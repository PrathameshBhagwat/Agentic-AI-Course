import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from typing import Annotated

load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

class outputStruct(BaseModel):
    name:Annotated[str,Field(description="this is for the user name")]
    age:Annotated[int,Field(description="this is for the users age")]
    contact:Annotated[int,Field(description="this is for users contact")]
    
output_format = model.with_structured_output(outputStruct)

result = output_format.invoke("My name is Prathamesh my ge is 23 and My contact number is 9988776655")

print(result)