from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

students = {1: {"name": "John", "age": 19, "class": "year 12"}}


class Student(BaseModel):
    name: str
    age: int
    year: str


# The decoretors signifies the HTTP method
@app.get("/")  # <-- The /home means endpoint HOME in a website's URL
def index():  # index() is the function that runs when the endpoint is accessed
    return {"name": "First Data"}

# Path parameter
@app.get("/get-student/{student_id}")  # get-student is an endpoint. just like /home
def get_student(
    student_id: int = Path(
        description="The ID of the student you want to view", gt=0, lt=3
    )
):  # student_id is like a variable that stores the value returned
    return students[
        student_id
    ]  # its specifying to return student_id / variable from the student

# Query parameter
@app.get("/get-by-name")
def get_student(name: str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found!"}

# Combining Path parameter and Query parameter
@app.get("/get-by-name/{student_id}")
def get_student(student_id: int, name: str):
    for student_id in students:  # Use a meaningful variable name in place of student_id
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found!"}

# Post Method using path and query parameter
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:  # if student { your value } already in list
        return {"Error": "Student already exist"}
    students[student_id] = student
    return students

@app.put()