import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Annotated

load_dotenv()

# Hugging Face Model
model = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

llm_model = ChatHuggingFace(llm=model)


# Pydantic Structure
class PatientInfo(BaseModel):

    name: Annotated[
        str,
        Field(description="Name of the patient")
    ]

    age: Annotated[
        int,
        Field(description="Age of the patient")
    ]

    symptoms: Annotated[
        list[str],
        Field(description="List of symptoms")
    ]


# Output Parser
parser = PydanticOutputParser(
    pydantic_object=PatientInfo
)


# Patient information
patient_information = """
Patient Ravi is 45 years old and has fever and cough.
"""


# Prompt
prompt = f"""
Extract the patient information from the following message.

Patient information:
{patient_information}

Return the result in the following format:

Name: Ravi
Age: 45
Symptoms: Fever, Cough

{parser.get_format_instructions()}
"""


# Invoke LLM
result = llm_model.invoke(prompt)


# Parse the response
final_result = parser.parse(result.content)


# Extract each value separately
print("Name:", final_result.name)
print("Age:", final_result.age)
print("Symptoms:", final_result.symptoms)