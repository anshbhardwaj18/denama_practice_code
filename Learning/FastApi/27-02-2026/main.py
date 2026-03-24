# from fastapi import FastAPI, Body
# from pydantic import BaseModel
# from typing import Annotated
# app = FastAPI()

##CREATE AND INSERT DATA
# #WITHOUT PYDANTIC MODEL
# @app.post("/product")
# async def create_product(new_product : dict):
#     return new_product

# # WITH PYDANTIC MODEL
# class Product(BaseModel):
#     id:int
#     name:str
#     price:float
#     stock: int | None = None

# @app.post("/product")
# async def create_product(new_product : Product):
#     return new_product

## ACCESS ATTRIBUTE INSIDE FUNCTION
# @app.post("/product")
# async def create_product(new_product : Product):
#     print(new_product.id)
#     print(new_product.name)
#     print(new_product.price)
#     print(new_product.stock)
#     return new_product

## ADD NEW CALCULATED ATTRIBUTES
# @app.get("/product")
# async def create_product(new_product : Product):
#     product_dict = new_product.model_dump()
#     price_with_tax = new_product.price + (new_product.price * 18/100)
#     product_dict.update({"price_with_tax" : price_with_tax})
#     return product_dict

## COMBINING REQUEST BODE WITH PATH PARAMETER
# @app.put("/products/{prouduct_id}")
# async def update_product(product_id : int, new_updated_product : Product):
#     return {"product_id" : product_id, "new_updated_product" : new_updated_product}

## ADDING QUERY PARAMETER
# @app.put("/products/{product_id}")
# async def update_product(product_id : int, new_updated_product : Product, discount: float | None = None):
#     return {"product_id" : product_id, "new_updated_product" : new_updated_product, "discount" : discount}


# ************************** MULTIPLE BODY PARAMETER ******************************** #
# class Product(BaseModel):
#     name: str
#     price: float
#     stock: int | None = None

# class Seller(BaseModel):
#     username : str
#     full_name : str | None = None

# @app.post("/product")
# async def create_product(product : Product, seller : Seller):
#     return {"Product" : product, "Seller" : seller}

## MAKE BODY OPTIONAL
# @app.post("/product")
# async def create_product(product : Product, seller : Seller | None = None):
#     return {"Product" : product, "Seller" : seller}

## SINGULAR VALUES IN BODY
# @app.post("/product")
# async def create_product(
#     product : Product, 
#     seller : Seller, 
#     sec_key : Annotated[str, Body()]
#     ):
#     return {"product" : Product, "seller" : Seller, "sec_key" : sec_key}