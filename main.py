from fastapi import FastAPI, Path, Query

app = FastAPI()

students = {
    1: {"name": "Abinaya", "age": 20, "year": "bachelor 2nd year"},
    2: {"name": "Nischal", "age": 13, "year": "year 6"},
    3: {"name": "Arjun", "age": 19, "year": "bachelor 1st year"},
    4: {"name": "Priya", "age": 22, "year": "masters 1st year"},
    5: {"name": "Kiran", "age": 10, "year": "year 3"},
    6: {"name": "Sara", "age": 17, "year": "year 12"},
    7: {"name": "Dev", "age": 15, "year": "year 9"},
    8: {"name": "Mitali", "age": 25, "year": "phd 2nd year"},
    9: {"name": "Zain", "age": 12, "year": "year 5"},
    10: {"name": "Rhea", "age": 21, "year": "bachelor 3rd year"},
}


@app.get("/")
def index():
    return "hello my name is Abinaya Pandey"


# @app.get("/stds_info/{student_id}")
# def get_info(student_id: int = Path (description="Input the id of the student")):
#     return students[student_id]


@app.get("/student_info/")
def get_info(std_id: int = Path(description="Enter student id", gt=0, lt=11)):
    if std_id not in students:
        return {"error": "Student not found"}
    return students[std_id]

