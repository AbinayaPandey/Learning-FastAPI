from fastapi import FastAPI, Path

app = FastAPI()

students = {1: {"name": "John", "age": 19, "class": "year 12"}}


# The decoretors signifies the HTTP method
@app.get("/")  # <-- The /home means endpoint HOME in a website's URL
def index():  # index() is the function that runs when the endpoint is accessed
    return {"name": "First Data"}


@app.get("/get-student/{student_id}")  # get-student is an endpoint. just like /home
def get_student(
    student_id: int = Path(
        description="The ID of the student you want to view", gt=0, lt=3
    )
):  # student_id is like a variable that stores the value returned
    return students[
        student_id
    ]  # its specifying to return student_id / variable from the student


@app.get("/get-by-name/{student_id}")
def get_student(student_id: int, name: str):
    for student_id in students:  # Use a meaningful variable name in place of student_id 
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found!"}
