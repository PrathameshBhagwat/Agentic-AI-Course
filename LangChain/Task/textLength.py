import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableBranch

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

def checkLength(sentence):
    return len(sentence.split())>10

branch_chain = RunnableBranch(
    (
        checkLength,
        lambda sentence: "Long Sentence"
    ),
    lambda sentence:"Short Sentence"
)

result = branch_chain.invoke(
    "I am learning LangChain and building AI applications every day"
)
print(result)