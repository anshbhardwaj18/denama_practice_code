from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError
app = FastAPI()

fruits = {
    "apple" : "A fruit juice",
    "banana" : "A yellow delight"
}

# items = {
#     "apple" : "A juice fruit",
#     "banana" : "A yellow color fruit"
# }

#USING HTTPException
# @app.get("/items/{items_id}")
# async def get_data(items_id: str):
#     if items_id not in items:
#         raise HTTPException(status_code=404, detail="Page not found")
#     return items[items_id]

# Custom Header
# @app.get("/items{items_id}")
# async def get_data(items_id : str):
#     if items_id not in items:
#         raise HTTPException(
#         status_code=404, 
#         detail="Page not found",
#         headers= {"x-error-type" : "itemmissing"}
#         )
#     return items[items_id]


# ********************************* CUSTOM EXCEPTION ************************************
# class fruitException(Exception):
#     def __init__(self, fruit_name : str):
#         self.fruit_name = fruit_name

# @app.exception_handler(fruitException)
# async def fruit_exception_handler(request : Request, exc : fruitException):
#     return JSONResponse(
#         status_code = 418,
#         content= {"message" : f"{exc.fruit_name} is not valid"}
#     )

# @app.get("/fruits/{fruit_name}")
# async def get_fruit(fruit_name : str):
#     if fruit_name not in fruits :
#         raise fruitException(fruit_name= fruit_name)
#     return fruits[fruit_name]


# ********************************* OVERRIDE DEFAULT EXCEPTION HANDLERS ****************
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc:RequestValidationError):
    return PlainTextResponse(str(exc), status_code=404)

@app.get("/items/{items_id}")
async def read_items(items_id : int):
    return items_id