# Task 1: Country
# • Input: Country name
# • Generate at the same time:
# o Capital
# o Population
# o One famous place


import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel , RunnableSequence

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

capital_prompt = ChatPromptTemplate.from_template(
    "What is the capital of {country}? Give only the capital name."
)

population_prompt = ChatPromptTemplate.from_template(
    "What is the population of {country}? Give a short answer."
)

place_prompt = ChatPromptTemplate.from_template(
    "Name one famous place in {country} and give one short description."
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "capital": RunnableSequence(
        capital_prompt,
        model,
        parser
    ),
    "population":RunnableSequence(
        population_prompt,
        model,
        parser
    ),
    "place":RunnableSequence(
        place_prompt,
        model,
        parser
    )
})

result = parallel_chain.invoke({
    "country" : "India"
})

print(result)