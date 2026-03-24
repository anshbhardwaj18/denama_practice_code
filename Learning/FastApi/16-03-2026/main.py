from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel
from typing import List, Any, Optional

app = FastAPI()

# class Product(BaseModel):
#     id : int
#     name : str
#     price : float
#     stock : int | None = None
# Without Return Type
# @app.get("/products/")
# async def get_products():
#     return [
#         {"Status" : "Ok"},
#         {"Status" : 200}
#     ]

# Return type Annotation
# @app.get("/products/")
# async def get_products() -> List[Product]:
#     return[
#         {"id" : 1, "name" : "Bag", "price" : 154.89, "stock" : 10},
#         {"id" : 2, "name" : "Bag-2", "price" : 155.89, "stock" : 9},
#         {"id" : 3, "name" : "Bag-3", "price" : 156.89, "stock" : 11},
#         {"id" : 4, "name" : "Bag-4", "price" : 157.89, "stock" : 6}
#     ]

# @app.post("/products/")
# async def create_product(product: Product) -> Product:
#     return product

# **************************** RESPONSE MODEL ********************************* #
class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int | None = None

class ProductOut(BaseModel):
    name : str
    price : float

# Without response_model parameter    
# @app.get("/products/")
# async def get_products():
#     return {"id" : 1, "name" : "Moto-E", "price" : 33.44, "stock" : 5}

# With response_model parameter
# @app.get("/products/", response_model=Product)
# async def get_product():
#     return {"id" : 1, "name" : "Moto-E", "price" : 33.44, "stock" : 5}

# @app.get("/products/", response_model=List[Product])
# async def get_product():
#     return [
#         {"id" : 1, "name" : "Moto-E", "price" : 33.44, "stock" : 5},
#         {"id" : 2, "name" : "Redmi Note-5", "price" : 19999.44, "stock" : 5}
#     ]

# @app.post("/product/", response_model=Product)
# async def create_product(product: Product):
#     return product

# class BaseUser(BaseModel):
#     username : str
#     fullname : str | None = None

# class UserIn(BaseUser):
#     password : str

# @app.post("/users/", response_model=BaseUser)
# async def create_user(user: UserIn):
#     return user

# @app.post("/product/", response_model=Product)
# async def create_product(product: Product) -> Any:
#     return product


# ********************** INCLUDE AND EXCLUDE SPECIFIC FIELD *************************** #   EXCLUDING UNSET DEFAULT VALUES
products_db = {
    "1" : {"id" : "1", "name" : "Laptop", "price" : 999.99, "stock" : 10, "is_active": True},
    "2" : {"id" : "2", "name" : "Mobile", "price" : 599.99, "stock" : 20, "is_active": False}
}

class Product(BaseModel):
    id: str
    name : str
    price : float
    description : Optional[str] = None
    tax : float = 15.0 # Default tex rate

# @app.get("/products/{product_id}", response_model=Product, response_model_exclude_unset=True)
# async def get_product(product_id : str):
#     return products_db.get(product_id, {})

# INCLUDE SPECIFIC FIELD
# @app.get("/products/{product_id}", response_model=Product, response_model_include={"name", "price"})
# async def get_product(product_id: str):
#     return products_db.get(product_id, {})

# EXCLUDE SPECIFIC FIELD
# @app.get("/products/{product_id}", response_model=Product, response_model_exclude={"name","price"})
# async def get_product(product_id: str):
#     return products_db.get(product_id, {})