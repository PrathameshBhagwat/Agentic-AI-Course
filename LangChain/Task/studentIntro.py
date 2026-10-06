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

intro_prompt = ChatPromptTemplate.from_template(
    "Give the short and creative introduction for the {name}"
)

parser = StrOutputParser()

intro_chain = RunnableSequence(
    intro_prompt,
    model,
    parser
)

parallel_chain = RunnableParallel({
    "name": RunnablePassthrough(),
    "intro": intro_chain
})

result = parallel_chain.invoke({
    "name":"Prathamesh"
})

print(result)