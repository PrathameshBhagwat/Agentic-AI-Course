from fastapi import FastAPI
from pydantic import BaseModel,Field,EmailStr
from typing import Annotated,List,Dict
from pymongo import MongoClient 
import json

connection = MongoClient("mongodb://localhost:27017/")

database = connection["StudentDB"]

collection = database["students"]

app = FastAPI()

class studentStructure(BaseModel):
    name:Annotated[str,Field(title="Enter your name")]
    roll:Annotated[int,Field(title="Enter your roll")]
    age: Annotated[int, Field(title="Enter your age")]
    year: Annotated[str, Field(title="Enter your year")]
    email: Annotated[EmailStr, Field(title="Enter your email")]
    subjects : Dict
    hobbies : List

 
@app.get("/")
def greet():
    return "Good Job"

@app.post("/add")
def add_stud(info:studentStructure):
    sname = info.name
    sroll = info.roll
    sage = info.age
    syear = info.year
    semail = info.email
    ssubjects = info.subjects
    shobbies = info.hobbies
    
    sinfo = {
        "name" : sname,
        "roll" : sroll,
        "age" : sage,
        "year" : syear,
        "email" : semail,
        "subjects" : ssubjects,
        "hobbies" : shobbies
    }
    
    
    with open("students.json","r") as f:
        students = json.load(f)
        
    students.append(sinfo)
    
    with open("students.json","w") as f:
        json.dump(students,f)
    
    collection.insert_one(sinfo)  
    
    return{"message":"new student stored in both mongo and json"}

@app.get("/allstudents")
def all_students():
    with open("students.json","r") as f:
        students = json.load(f)
    
    return students

@app.get("/student/name/{name}")
def find_student_name(name : str):
    with open("students.json","r") as f:
        students = json.load(f)
        
    for i in students:
        if i["name"] == name:
            return i 
    
    return {"message" : "Student not found"}

@app.get("/student/roll/{roll}")
def find_student_roll(roll : int):
    with open("students.json","r") as f:
        students = json.load(f)
    
    for i in students:
        if i["roll"] == roll:
            return i 
    
    return {"message" : "Student not found"}