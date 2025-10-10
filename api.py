from fastapi import FastAPI, HTTPException, status, Query

app = FastAPI()

items = {1: {"name":"Milk", "price":60, "brand":"Amul"},
         2: {"name":"Chicken", "price":450, "brand":"Boiler"},
         3: {"name":"Masala", "price":200, "brand":"Nepali"}}

@app.get("/")
def index():
    return "This is an index page"

@app.get("/get-by-id/{items_id}")
def get_by_id(items_id: int):
    if items_id not in items:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Item with id '{items_id}' not found")
        # return {"Error":"Item not found!"}
    return items[items_id]

@app.get("/get-by-name/")
def get_by_name(name: str = Query(description="Enter the name of the item you want to display")):
    for item in items:
        if items[items]["name"].lower() = name.lower()
    # if name not in items:
    #     raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Name '{name}' not found in the item list")
    # return items[name]