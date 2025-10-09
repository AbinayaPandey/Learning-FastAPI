from fastapi import FastAPI, Path, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

# std_info = {1: {"name": "Abinaya", "age": 20, "ethnicity": "hindu"},
#             2: {"name":"Nischal", "age": 13, "ethnicity":"hindu"}}
std_info = {

}

class Std_info(BaseModel):
    id: int
    name: str
    ethnicity: str


@app.get("/")
def index():
    return {"Hello to the index page"}


@app.get("/info_by_id/")
def info_by_id(std_id: int):
    if std_id not in std_info:
        return {"Error": "Id doesn't exist"}
    return std_info[std_id]


# @app.get("/info_by_name/")
# def info_by_name(name: str):
#     for std_id in std_info:
#         if std_info[std_id]["name"].lower() == name.lower():
#             return std_info[std_id]
#     return {"Error": "Name doesn't exist"}

@app.get("/info_by_id_name/{std_id}")
def info_by_id(name: str, std_id: int):
    if std_id not in std_info:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail= f"Info with id {std_id} not in the list")
    elif std_info[std_id].name.lower() != name.lower():
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=f"Student name '{name}' doesn't match with id '{std_id}'")
    return std_info[std_id]

@app.post("/post_by_id/{std_id}")
def post_by_id(students: Std_info, std_id: int):  # students: Std_info - its creating object of the class Std_info
    if std_id in std_info:
        # raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=f"Student id '{students.id}' already exists") # . operator is used to specify object
        return {"Error":f"Student id '{students.id}' already exists"}
    std_info[std_id] = students.model_dump()
    return std_info[std_id]
    # return {"message": f"student info of ''posted successfully "}
