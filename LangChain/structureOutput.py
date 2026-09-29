import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from pydantic import BaseModel, Field
from typing import Annotated
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")
load_dotenv()

model = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

class personStruct(BaseModel):
    name: Annotated[str, Field(description="give user name here")]
    age: Annotated[int, Field(description="give user age here")]
    contact: Annotated[int, Field(description="give user contact here")]

parser = PydanticOutputParser(pydantic_object=personStruct)
llm_model = ChatHuggingFace(llm=model)
prompt = f"my name is demouser my age is 22 my contact number is 8989898989 {parser.get_format_instructions()}"

result = llm_model.invoke(prompt)
print(result.content)
