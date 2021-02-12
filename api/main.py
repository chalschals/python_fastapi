from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
fackdb = []

class Course(BaseModel):
    id:int
    name:str
    price:float
    is_active: Optional[bool] = None
    # is_active: bool

@app.get("/")
def read_root():
    return {"greetings":"some greetings"}

@app.get("/courses")
def get_courses():
    return fackdb

@app.get("/courses/{course_id}")
def get_a_course(course_id:int):
    return fackdb[course_id-1]

@app.post("/courses/")
def create_course(course:Course):
    fackdb.append(course.dict())
    return fackdb[-1]


@app.delete("/courses/{course_id}")
def delete_course(course_id:int):
    fackdb.pop(course_id-1)
    return {"task":"deletion success"}