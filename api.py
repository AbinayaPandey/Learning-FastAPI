from fastapi import FastAPI, HTTPException, status, Query
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

inventory = {1: {"name":"Milk", "price":60, "brand":"Amul"},
         2: {"name":"Chicken", "price":450, "brand":"Boiler"},
         3: {"name":"Masala", "price":200, "brand":"Nepali"}}
# inventory = {
#     ''' an empty item dictionary so that when you post items you have an empty place to dump values.
#     Since items dict is empty that means you cant use get items by id / name before posting the value first.
#     and since the values in the dictionary is erased as soon as the page is relaod, its impossible to get items before posting.
#     '''
# }

class Item(BaseModel):
    name: str
    price: int 
    brand: Optional[str] = None

@app.get("/")
def index():
    return "This is an index page"

@app.get("/get-by-id/{items_id}")
def get_by_id(items_id: int):
    if items_id not in inventory:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Item with id '{items_id}' not found")
        # return {"Error":"Item not found!"}
    return inventory[items_id]

@app.get("/get-by-name/")
def get_by_name(name: str = Query(description="Enter the name of the item you want to display")):
    for item in inventory:
        if inventory[item]["name"].lower() == name.lower():
            return inventory[item]
    raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f"Name '{name}' not found in the item list",)


@app.post("/post-by-id/")
def post_by_id(item_id: int, things: Item):
    if item_id in inventory:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Item id '{item_id}' already in the list")
    inventory[item_id] = things.model_dump()
    return inventory[item_id]

