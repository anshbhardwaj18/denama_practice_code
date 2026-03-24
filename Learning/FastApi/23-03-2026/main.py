from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

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
class fruitException(Exception):
    def __init__(self, fruit_name : str):
        self.fruit_name = fruit_name