import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from pydantic import BaseModel, Field
from typing import Annotated, List
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
    symptoms: Annotated[List[str], Field(description="List of symptoms the patient is suffering from")]
    blood_group : Annotated[str,Field(description="Blood group of the patient")]
    
    
parser = PydanticOutputParser(pydantic_object=personStruct)
llm_model = ChatHuggingFace(llm=model)

patient_information = """
 Patient name is Priya Sharma, age 35, suffering from fever and headache. Her
blood group is O+."""

prompt = f"""
Extract the patient information from the following text.

Patient information:
{patient_information}

Return the information according to the required format.

{parser.get_format_instructions()}"""



result = llm_model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)