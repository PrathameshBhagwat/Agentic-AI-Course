import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv(dotenv_path=Path(__file__).resolve().parent / ".env")
load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

context = []
condition = True

while condition == True:
    ques= input("Enter your question : ").strip()
    
    print(context)
    if ques.lower() == "exit":
        print("GoodBye")
        break
    else:
        context.append(HumanMessage(content=ques))
        try:
            res = model.invoke(context )
            print(res.text)
        
            context.append(AIMessage(content=res.text))
        except Exception as e :
            print(e)
            context.pop()