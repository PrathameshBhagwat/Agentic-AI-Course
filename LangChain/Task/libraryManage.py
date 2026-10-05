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

class BookStruct(BaseModel):
    book_name: Annotated[str,Field(description="Name of the book")]

    author: Annotated[str,Field(description="Author of the book")]

    pages: Annotated[int,Field(description="Number of pages in the book")]

    category: Annotated[str,Field(description="Category of the book")]

    available: Annotated[bool,Field(description="Whether the book is available for issuing")]

parser = PydanticOutputParser(pydantic_object=BookStruct)


# User Input
book_information = """
I want to issue the book Python Programming by Mark Lutz.
It has 800 pages and belongs to the programming category.
"""


# Prompt
prompt = f"""
Extract the book information from the following message.

Message:
{book_information}

The user wants to issue this book, so set available to true.

Return the information according to the required format.

{parser.get_format_instructions()}
"""


# Invoke LLM
result = llm_model.invoke(prompt)


# Parse the response
final_result = parser.parse(result.content)


# Display result
print(final_result)