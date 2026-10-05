import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from pydantic import BaseModel, Field
from typing import Annotated
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

model = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

class personStruct(BaseModel):
    name: Annotated[str, Field(description="give user name here")]
    age: Annotated[int, Field(description="give user age here")]
    course: Annotated[str, Field(description="give user course here")]
    year: Annotated[int, Field(description="Give the year now")]
    percentage: Annotated[float, Field(description="Give me the percentage in the course")]
    
    
parser = PydanticOutputParser(pydantic_object=personStruct)
llm_model = ChatHuggingFace(llm=model)
prompt = f"""
Extract the following information and return it according to the required format.

My name is Gagandip, I am 21 years old, studying Computer Science in 3rd year,
and my percentage is 78.5.

{parser.get_format_instructions()}
"""

result = llm_model.invoke(prompt)

print(result.content)