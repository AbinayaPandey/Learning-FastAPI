from fastapi import FastAPI, HTTPException, status, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# std_info = {1: {"name": "Abinaya", "age": 20, "ethnicity": "hindu"},
#             2: {"name":"Nischal", "age": 13, "ethnicity":"hindu"}}
std_info = {

}

class Std_info(BaseModel):
    id: int = None
    name: str
    ethnicity: str

class Updated_info(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    ethnicity: Optional[str] = None


@app.get("/")
def index():
    return {"Hello to the index page"}


@app.get("/info-by-id/")
def info_by_id(std_id: int):
    if std_id not in std_info:
        return {"Error": "Id doesn't exist"}
    return std_info[std_id]


# @app.get("/info-by-name/")
# def info_by_name(name: str):
#     for std_id in std_info:
#         if std_info[std_id]["name"].lower() == name.lower():
#             return std_info[std_id]
#     return {"Error": "Name doesn't exist"}

@app.get("/info-by-id-name/{std_id}")
def info_by_id(name: str, std_id: int):
    if std_id not in std_info:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail= f"Info with id {std_id} not in the list")
    elif std_info[std_id]["name"].lower() != name.lower():
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=f"Student name '{name}' doesn't match with id '{std_id}'")
    return std_info[std_id]

@app.post("/post-by-id/{std_id}")
def post_by_id(students: Std_info, std_id: int):  # students: Std_info - its creating object of the class Std_info
    if std_id in std_info:
        # raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=f"Student id '{students.id}' already exists") # . operator is used to specify object
        return {"Error":f"Student id '{students.id}' already exists"}
    std_info[std_id] = students.model_dump()
    return std_info[std_id]
    # return {"message": f"student info of ''posted successfully "}

@app.put("/put-by-id/{std_id}")
def put_by_id(std_id: int, students: Updated_info):  # students: Std_info because you are to access Std_info class that specify the type of data to be entered
    if std_id not in std_info:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Student with id '{std_id}' not found in the list")
    
    if students.name is not None:
        std_info[std_id]["name"] = students.name
    if students.ethnicity is not None:
        std_info[std_id]["ethnicity"] = students.ethnicity
    if students.id is not None:
        std_info[std_id]["id"] = students.id

    return {"message":f"Students info for id {std_id} has been updated"}

@app.delete("/delete-info/")
def delete_info(std_id: int):
    if std_id not in std_info:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f"Student with id '{std_id}' not found in the list",)

    del std_info[std_id]
    return {"message": f"Info of the student {std_id} deleted successfully"}