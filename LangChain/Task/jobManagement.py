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


# 2. Define Pydantic Structure
class ApplicantStruct(BaseModel):

    name: Annotated[
        str,
        Field(description="Name of the job applicant")
    ]

    experience: Annotated[
        int,
        Field(description="Total years of work experience")
    ]

    skills: Annotated[
        list[str],
        Field(description="Technical skills of the applicant")
    ]

    expected_salary: Annotated[
        float,
        Field(description="Expected salary in LPA")
    ]

    immediate_joiner: Annotated[
        bool,
        Field(description="Whether the applicant can join immediately")
    ]


# 3. Create Pydantic Parser
parser = PydanticOutputParser(
    pydantic_object=ApplicantStruct
)


# 4. User Input
applicant_information = """
My name is Amit Patil.
I have 2 years of experience in React and Node.js.
I am expecting a salary of 6 LPA and can join immediately.
"""


# 5. Create Prompt
prompt = f"""
Extract the job applicant information from the following message.

Applicant information:
{applicant_information}

The expected salary should be represented as a number in LPA.

Return the information according to the required format.

{parser.get_format_instructions()}
"""


# 6. Invoke LLM
result = llm_model.invoke(prompt)


# 7. Parse LLM response
final_result = parser.parse(result.content)


# 8. Display result
print(final_result)