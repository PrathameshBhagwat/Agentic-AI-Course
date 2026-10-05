import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

parser = StrOutputParser()


prompt1 = ChatPromptTemplate.from_template(
    "Give a short and simple description of the movie {movie}"
)

description_chain = prompt1 | model | parser


prompt2 = ChatPromptTemplate.from_template(
    "Give the main characters of the movie {movie}"
)

characters_chain = prompt2 | model | parser


prompt3 = ChatPromptTemplate.from_template(
    "Give a short and interesting review of the movie {movie}"
)

review_chain = prompt3 | model | parser


parallel_chain = RunnableParallel(
    description=description_chain,
    characters=characters_chain,
    review=review_chain
)


movie = input("Enter Movie Name: ")

result = parallel_chain.invoke({"movie": movie})


print("Movie Description:")
print(result["description"])

print("==============================")

print("Main Characters:")
print(result["characters"])

print("==============================")

print("Movie Review:")
print(result["review"])