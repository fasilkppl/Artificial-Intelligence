from fastapi import FastAPI

from enum import Enum

app = FastAPI()


# creating a endpoint in url named hello
@app.get("/hello")
async def hello():
    return "Welcome" # welcome is display as a msg on screen ie, Visiting /hello returns the message "Welcome"

# creating a endpoint in url named hello and afterward whatever the user enters becomes the next end point
@app.get("/hello/{name}")
async def hello(name):
    return f"Welcome {name}" # it will take whatever the user enters and display along welcome <user enters>





coupon_code = {
    1: '10%',
    2: '20%',
    3: '30%'
}

@app.get("/get_coupon/{code}")
async def get_items(code: int): # what user enters must be an integer, if yes get coupon_code associated with it.
    return { 'discount_amount': coupon_code.get(code) }




# This means your API only accepts these three cuisine types.
class AvailableCuisines(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"

#This is a simple lookup table.
food_items = {
    'indian' : [ "Samosa", "Dosa" ],
    'american' : [ "Hot Dog", "Apple Pie"],
    'italian' : [ "Ravioli", "Pizza"]
}

# The {cuisine} must be one of: indian, american, italian
# FastAPI automatically validates this. (no need of if statements)
@app.get("/get_items/{cuisine}")
async def get_items(cuisine: AvailableCuisines): # if cusine (what user enters) is available in AvailableCuisines class, then it will look food_items and give appropriate values related to keys.
    return food_items.get(cuisine)


# to run this file   (uvicorn FastAPI:app --reload)
