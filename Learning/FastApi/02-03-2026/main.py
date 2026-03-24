# from fastapi import FastAPI
# from pydantic import BaseModel, Field
# from typing import Annotated

# app = FastAPI()

# class Product(BaseModel):
#     name:str = Field(
#         title= "Product name",
#         description= "The name of the product",
#         max_length= 100,
#         min_length= 3
#     )
#     price: float = Field(
#         gt= 0,
#         title= "Product Price",
#         description="The price of the product in USD, must be greater than zero"
#     )
#     stock: int | None = Field(
#         default=None,
#         ge= 0,
#         title= "Stock quantity",
#         description= "The number of item in stock, must be non-negative"
#     )
# @app.post("/product")
# async def create_product(product: Product):
#     return product

# class Category(BaseModel):
#     name : str = Field(
#         title= "Category name",
#         description= "The name of the product category",
#         max_length=50,
#         min_length=1 
#     )
#     description: str | None = Field(
#         default= None,
#         title= "Category Description",
#         description= "A brief description of the category",
#         max_length= 200
#     )
# class Product(BaseModel):
#     name : str = Field(
#         title= "Product name",
#         description= "The name of the product",
#         max_length=100,
#         min_length=1
#     )
#     price : float = Field(
#         gt= 0,
#         title= "Product Price",
#         description= "The price in USD must be greater than zero"
#     )
#     stock : int | None = Field(
#         default= None,
#         ge= 0,
#         title= "Stock Quantity",
#         description= " Number of items in stock must be non-negative"
#     )
#     category : Category | None = Field(
#         default= None,
#         title= "Product Category",
#         description= "The category to which the product belongs"
#     )
# @app.post("/products")
# async def create_product(product: Product):
#     return product

# ************************ PYDANTIC BODY EXAMPLE VALUE *********************************
# ***************** USIDN FIELD(EXAMPLE=)
# class Product(BaseModel):
#     name : str = Field(examples=["Moto E"])
#     price : float = Field(examples= [23.56])
#     stock : int | None = Field(default=None, examples=[43])

# @app.post("/product")
# async def create_product(product : Product):
#     return product

# *********************** USING JSON 
# class Product(BaseModel):
#     name : str
#     price : float
#     stock : int | None = None

#     model_config = {
#         "json_schema_extra":{
#             "examples":[
#                 {
#                     "name" : "Moto E",
#                     "price" : 34.56,
#                     "stock" :45
#                 }
#             ]
#         }
#     }