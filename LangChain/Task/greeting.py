# 1. RunnableSequence
# Task 1: Greeting
# • Input: Name
# • Step 1: Generate a greeting.
# • Step 2: Generate a short message using the greeting. 

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

greeting_prompt = ChatPromptTemplate.from_template(
    "Generate the simple greeting for {name}."
)

greeting_parser = StrOutputParser()

greeting_chain = RunnableSequence(
    greeting_prompt,
    model,
    greeting_parser
)

message_prompt = ChatPromptTemplate.from_template(
    "Using this greeting: {greeting},"
    "generate a short friendly message."
)

def prepare_message(greeting):
    return {
        "greeting": greeting
    }


message_chain = RunnableSequence(
    prepare_message,
    message_prompt,
    model,
    StrOutputParser()
)

greeting = greeting_chain.invoke({
    "name":"Prathamesh"
})

result = message_chain.invoke(greeting)

print(result)