import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Annotated

load_dotenv()

model = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

llm_model = ChatHuggingFace(llm=model)

class StudentResult(BaseModel):

    name: Annotated[
        str,
        Field(description="Name of the student")
    ]

    python: Annotated[
        int,
        Field(description="Marks obtained in Python")
    ]

    javascript: Annotated[
        int,
        Field(description="Marks obtained in JavaScript")
    ]

    dbms: Annotated[
        int,
        Field(description="Marks obtained in DBMS")
    ]

    total: Annotated[
        int,
        Field(description="Total marks obtained in all subjects")
    ]

    percentage: Annotated[
        float,
        Field(description="Percentage calculated from the three subjects")
    ]


parser = PydanticOutputParser(
    pydantic_object=StudentResult
)


prompt = f"""
Generate the result of the following student.

Student Prathamesh has scored:
Python: 85
JavaScript: 78
DBMS: 90

Calculate:
1. Total marks
2. Percentage

Each subject is out of 100.

Return the result according to the required format.

{parser.get_format_instructions()}
"""


# 5. Invoke LLM
result = llm_model.invoke(prompt)


# 6. Parse LLM response
final_result = parser.parse(result.content)


# 7. Extract each value separately
print("Name:", final_result.name)
print("Python:", final_result.python)
print("JavaScript:", final_result.javascript)
print("DBMS:", final_result.dbms)
print("Total:", final_result.total)
print("Percentage:", final_result.percentage)