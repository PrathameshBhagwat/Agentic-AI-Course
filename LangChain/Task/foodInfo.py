# Task 2: Food
# • Input: Food name
# • Step 1: Generate a short description.
# • Step 2: Generate 3 benefits using the description. 

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

description_prompt = ChatPromptTemplate.from_template(
    "Generate the short description for the following food item {name}"
)

description_parser = StrOutputParser()

description_chain = RunnableSequence(
    description_prompt,
    model,
    description_parser
)

benefits_prompt = ChatPromptTemplate.from_template(
    "Using the description: {description},"
    "generate a pointwise and clear 3 benefits."
)

def prepare_benefits(description):
    return{
        "description" : description
    }
    
benefits_chain = RunnableSequence(
    prepare_benefits,
    benefits_prompt,
    model,
    StrOutputParser()
)

description = description_chain.invoke({
    "name":"Dal and Rice"
})

result = benefits_chain.invoke(description)

print(result)