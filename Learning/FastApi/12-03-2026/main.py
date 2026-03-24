from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()

#Header Parameter
# @app.get("/product")
# async def get_product(user_agent : Annotated[str|None, Header()]=None):
#     return user_agent
# curl -H "User-Agent: Mozilla/5.0" http://127.0.0.1:8000/product

# HANDLING DUPLICATE HEADERS
# @app.get("/products")
# async def get_product(x_product_token: Annotated[list[str] | None, Header()] = None):
#     return {
#         "x_product_token" : x_product_token or []
#     }

## HEADER WITH PYDANTIC MODEL
# class ProductHeader(BaseModel):
#     authorization : str
#     accept_language : str | None = None
#     x_tracking_id : list[str] = []

# @app.get("/products")
# async def get_product(headers : Annotated[ProductHeader, Header()]):
#     return {
#         "headers" : headers
#     }
# curl -H "Authorization: Bearer token123" -H "Accept-Language: en-us" -H "X-Tracking-Id: track1" -H "X-Tracking-Id: track2" http://127.0.0.1:8000/products

# FORBIDDING EXTRA HEADERS
class ProductHeader(BaseModel):
    model_config = {"extra":"forbid"}
    authorization : str
    accept_language : str | None = None
    x_tracking_id : list[str] = []

@app.get("/products")
async def get_product(headers : Annotated[ProductHeader, Header()]):
    return {
        "headers" : headers
    }
#>curl -H "Authorization: Bearer token123" -H "Accept-Language: en-us" -H "X-Tracking-Id: track1" -H "X-Tracking-Id: track2" -H "extra-header: h123" http://127.0.0.1:8000/products