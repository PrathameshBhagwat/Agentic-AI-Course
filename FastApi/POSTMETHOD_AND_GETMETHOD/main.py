from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from typing import Annotated, List, Dict, Optional
from pymongo import MongoClient
import json

connection = MongoClient("mongodb://localhost:27017/")
database = connection["StudentDB"]
collection = database["students"]

app = FastAPI()

class studentStructure(BaseModel):
    name: Annotated[str, Field(title="Enter your name")]
    roll: Annotated[int, Field(title="Enter your roll")]
    age: Annotated[int, Field(title="Enter your age")]
    year: Annotated[str, Field(title="Enter your year")]
    email: Annotated[EmailStr, Field(title="Enter your email")]
    subjects: Dict
    hobbies: List


@app.get("/")
def greet():
    return "Good Job"

@app.post("/add")
def add_student(info: studentStructure):
    sname = info.name
    sroll = info.roll
    sage = info.age
    syear = info.year
    semail = info.email
    ssubjects = info.subjects
    shobbies = info.hobbies

    sinfo = {
        "name": sname,
        "roll": sroll,
        "age": sage,
        "year": syear,
        "email": str(semail),
        "subjects": ssubjects,
        "hobbies": shobbies
    }

    with open("students.json", "r") as f:
        students = json.load(f)
    students.append(sinfo)

    with open("students.json", "w") as f:
        json.dump(students, f, indent=4)
        
    collection.insert_one(sinfo)
    return {"message": "New student stored in both MongoDB and JSON"}
    

@app.get("/allstudents")
def all_students():
    # with open("students.json", "r") as f:
    #     students = json.load(f)
    # return students
    alldata = list(collection.find({},{"name":1,"roll":1,"age":1,"year":1,"email":1,"subjects":1,"hobbies":1,"_id":0}))
    return alldata


@app.get("/student/name/{name}")
def find_student_name(name: str):
    # with open("students.json", "r") as f:
    #     students = json.load(f)
    students = list(collection.find({},{"name":1,"roll":1,"age":1,"year":1,"email":1,"subjects":1,"hobbies":1,"_id":0}))
    for student in students:
        if student["name"] == name:
            return student
    return {"message": "Student not found"}


@app.get("/student/roll/{roll}")
def find_student_roll(roll: int):
    # with open("students.json", "r") as f:
    #     students = json.load(f)
    students=list(collection.find({},{"name":1,"roll":1,"age":1,"year":1,"email":1,"subjects":1,"hobbies":1,"_id":0}))
    for student in students:
        if student["roll"] == roll:
            return student
    return {"message": "Student not found"}


# THE PUT METHOD 
class UpdateStructure(BaseModel):
    name: Annotated[Optional[str],Field(title="Enter your name",default=None)]
    age: Annotated[Optional[int], Field(title="Enter your age",default=None)]
    year: Annotated[Optional[str], Field(title="Enter your year",default=None)]
    email: Annotated[Optional[EmailStr], Field(title="Enter your email",default=None)]

@app.put("/edit/{roll}")
def edit_student(roll: int,updateinfo : UpdateStructure):
    with open("students.json","r") as f:
        alldata = json.load(f)
        
    for i in alldata:
        if i["roll"]==roll:
            if updateinfo.name != None:
                i["name"] = updateinfo.name

            if updateinfo.age != None:
                i["age"] = updateinfo.age
    
            if updateinfo.year != None:
                i["year"] = updateinfo.year

            if updateinfo.email != None:
                i["email"] = updateinfo.email
                

        
                
    with open("students.json","w") as f2:
        json.dump(alldata,f2)

    #MongoDB implementations    
    updated_data = {}
    
    if updateinfo.name != None:
        updated_data["name"] = updateinfo.name
    
    if updateinfo.age != None:
        updated_data["age"] = updateinfo.age    

    if updateinfo.year != None:
        updated_data["year"] = updateinfo.year
        
    if updateinfo.email != None:
        updated_data["email"] = str(updateinfo.email)
        
    collection.update_one(
        {"roll": roll},
        {"$set": updated_data}
    )


    return {"message" : "The student updated."}


# Delete method 
@app.delete("/remove/{roll}")
def remove_student(roll: int):


    result = collection.delete_one({"roll": roll})


    with open("students.json", "r") as file:
        information = json.load(file)

    for i in information:
        if i["roll"] == roll:
            information.remove(i)
            break

    with open("students.json", "w") as file2:
        json.dump(information, file2, indent=4)



    if result.deleted_count == 0:
        return {"message": "Student not found"}

    return {"message": "Student deleted successfully"}      
    
    