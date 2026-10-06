# Task 2: Programming Language
# • Input: Programming language
# • Generate at the same time:
# o Definition
# o 3 features
# o One use 

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

definition_prompt = ChatPromptTemplate.from_template(
    "Give the definition of the following programming language topic {topic}"
)

features_prompt = ChatPromptTemplate.from_template(
    "Give the 3 clear and professional features of the following topic {topic}"
)

use_prompt = ChatPromptTemplate.from_template(
    "Give me the one use of the following topic {topic}"
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "definition": RunnableSequence(
        definition_prompt,
        model,
        parser
    ),
    "features":RunnableSequence(
        features_prompt,
        model,
        parser
    ),
    "use":RunnableSequence(
        use_prompt,
        model,
        parser
    )
})

result = parallel_chain.invoke({
    "topic" : "Python"
})

print(result)