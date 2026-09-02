from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hello World"

@app.get("/about")
async def about():
    return "These side Prathamesh"