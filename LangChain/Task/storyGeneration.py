import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

parser = StrOutputParser()

prompt1 = ChatPromptTemplate.from_template(
    "Create an attractive and professional story title about {topic}"
)

story_title = prompt1 | model | parser 

prompt2 = ChatPromptTemplate.from_template(
    """Write a proper, creative and attractive story based on the following title:
    {title}
    """
)

story_content = prompt2 | model | parser

prompt3 = ChatPromptTemplate.from_template(
    """Write a proper and interesting moral from the following story: 
    
    {story_content}
    """
)

story_moral = prompt3 | model | parser

topic = input("Enter Topic: ")

title = story_title.invoke({"topic":topic})

content = story_content.invoke({"title":title})

moral = story_moral.invoke({"story_content": content})

print(title)
print("==============================")
print(content)
print("==============================")
print(moral)