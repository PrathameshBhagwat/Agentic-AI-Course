# Task 2: Product
# • Input: Product name.
# • Use RunnablePassthrough() to keep the original product name.
# • At the same time, generate a short description. 

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough,RunnableSequence,RunnableParallel

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

description_prompt = ChatPromptTemplate.from_template(
    "Give the short and professional description for the {product}"
)

parser = StrOutputParser()

intro_chain = RunnableSequence(
    description_prompt,
    model,
    parser
)

parallel_chain = RunnableParallel({
    "product": RunnablePassthrough(),
    "description": intro_chain
})

result = parallel_chain.invoke({
    "product":"Dell Latitude 7400 Laptop"
})

print(result)