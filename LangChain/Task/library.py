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
class BookInfo(BaseModel):

    book: Annotated[
        str,
        Field(description="Name of the book")
    ]

    author: Annotated[
        str,
        Field(description="Author of the book")
    ]

    pages: Annotated[
        int,
        Field(description="Number of pages in the book")
    ]

    category: Annotated[
        str,
        Field(description="Category of the book")
    ]


# 3. Create Output Parser
parser = PydanticOutputParser(
    pydantic_object=BookInfo
)


# 4. Input Information
book_information = """
Harry Potter was written by J.K. Rowling.
It has 500 pages and belongs to the Fantasy category.
"""


# 5. Create Prompt
prompt = f"""
Extract the book information from the following text.

Book information:
{book_information}

Return the information according to the required format.

{parser.get_format_instructions()}
"""


# 6. Invoke LLM
result = llm_model.invoke(prompt)


# 7. Parse LLM Response
final_result = parser.parse(result.content)


# 8. Extract Each Field Separately
print("Book:", final_result.book)
print("Author:", final_result.author)
print("Pages:", final_result.pages)
print("Category:", final_result.category)