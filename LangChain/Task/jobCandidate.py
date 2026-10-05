import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Annotated

load_dotenv()

# 1. Hugging Face Model
model = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

llm_model = ChatHuggingFace(llm=model)


# 2. Create Pydantic Structure
class CandidateInfo(BaseModel):

    name: Annotated[
        str,
        Field(description="Name of the candidate")
    ]

    role: Annotated[
        str,
        Field(description="Job role of the candidate")
    ]

    experience: Annotated[
        int,
        Field(description="Years of experience")
    ]

    skills: Annotated[
        list[str],
        Field(description="Technical skills of the candidate")
    ]

    expected_salary: Annotated[
        float,
        Field(description="Expected salary in LPA")
    ]


# 3. Create Output Parser
parser = PydanticOutputParser(
    pydantic_object=CandidateInfo
)


# 4. Input Information
candidate_information = """
Sneha is a Python developer with 3 years of experience.
She knows Python, Django and SQL and expects 7 LPA.
"""


# 5. Create Prompt
prompt = f"""
Extract the candidate information from the following text.

Candidate information:
{candidate_information}

Return the information according to the required format.

{parser.get_format_instructions()}
"""


# 6. Invoke LLM
result = llm_model.invoke(prompt)


# 7. Parse LLM Response
final_result = parser.parse(result.content)


# 8. Extract Each Field Separately
print("Name:", final_result.name)
print("Role:", final_result.role)
print("Experience:", final_result.experience)
print("Skills:", final_result.skills)
print("Expected Salary:", final_result.expected_salary)