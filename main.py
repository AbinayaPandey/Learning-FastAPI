from fastapi import FastAPI, Path

app = FastAPI()

std_info = {1: {"name": "Abinaya", "age": 20, "ethnicity": "hindu"}}


@app.get("/")
def index():
    return {"Hello to the index page"}


@app.get("/info_by_id")
def info_by_id(std_id: int):
    if std_id not in std_info:
        return {"Error": "Id doesn't exist"}
    return std_info[std_id]


@app.get("/info_by_name")
def info_by_name(name: str):
    for std_id in std_info:
        if std_info[std_id]["name"].lower() == name.lower():
            return std_info[std_id]
    return {"Error": "Name doesn't exist"}
