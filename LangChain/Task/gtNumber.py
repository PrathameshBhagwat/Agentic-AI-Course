import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

def check_number(number):
    if number>50:
        return True
    else:
        return False
    
branch_chain = RunnableBranch(
    (
        check_number,
        lambda number: "Number is greater than 50"
    ),
    lambda number: "Number is less than 50"
)

result = branch_chain.invoke(75)
print(result)