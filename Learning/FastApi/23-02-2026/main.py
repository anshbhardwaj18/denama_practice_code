# ********************************** QUERY PARAMETER *************************
from fastapi import FastAPI, Path, Query
from typing import Annotated
# from pydantic import AfterValidator

app = FastAPI()

# SINGLE QUERY PARAMETER
# @app.get("/product")
# async def product(category : str):
#     return {"Status" : "Ok", "category" : category}

# MULTIPPLE QUERY PARAMETER
# @app.get("/products")
# async def product(category : str, limit : int):
#     return {"Status" : "Ok", "Category" : category, "limit" : limit}

# DEFAULT QUERY PARAMETER
# @app.get("/items")
# async def products(category : str, limit : int=15):
#     return {"Status" : "Ok", "Category" : category, "limit" : limit}

# OPTIONAL QUERY PARAMETER
# @app.get("/store")
# async def item(limit:int,category : str | None=None):
#     return {"Status" : "Ok", "limit" : limit, "Category" : category}

# PATH AND QUERY PARAMETER
# @app.get("/Shop/{year}")
# async def item(year:str,category:str):
#     return {"Status" : "Ok", "Year" : year, "category" : category}

# ****************************** RESPONSE STATUS CODE ***********************************
# PRODUCTS = [
    # {
    #     "id" : 1,
    #     "title" : "HP Omnibook 5 OLED, Snapdragon X Processor",
    #     "Price" : 109.85,
    #     "discription" : "Processor, Memory & Storage: Snapdragon X X1-26-100 (up to 2.97 GHz, 8 cores) | Memory: Snapdragon X X1-26-100 (up to 2.97 GHz, 8 cores) | Storage: 1 TB PCIe NVMe M.2 SSD"
    # },
    # {
    #     "id" : 2,
    #     "title" : "ASUS Vivobook Go 14, AMD Ryzen 3 7320U",
    #     "Price" : 200.89,
    #     "discription" : "Processor : AMD Ryzen 3 7320U Processor 2.4GHz (6MB Cache, up to 4.1GHz, 4 cores, 8 Threads) Display : 14.0-inch, FHD (1920 x 1080) 16:9 aspect ratio, 60Hz refresh rate, 250nits Brightness | Keyboard : Chiclet Keyboard"
    # },
    # {
    #     "id" : 3,
    #     "title" : "Dell 15, Intel Core 3, 14th Gen-100U, 8GB DDR4",
    #     "Price" : 100.95,
    #     "discription" : "Processor: Intel Core 3 100U 14th Generation (up to 4.70 GHz, 10MB 6 Cores)RAM & Storage: 8 GB, 1 x 8 GB, DDR4, 2666 MT/s & 512GB SSD Software: Pre-Loaded Windows 11 Home with Lifetime Validity | MS Office Home and Student 2024 with lifetime validity| McAfee Multi-Device Security 12-month subscription Graphics & Keyboard: Intel UHD Graphics & Standard Keyboard"
    # },
# ]

# GET REQUEST
# READ AND FETCH ALL DATA
# ALL DATA FETCH
# @app.get("/product", status_code=status.HTTP_200_OK)
# async def read_data():
#     return PRODUCTS

# SINGLE DATA FETCH
# @app.get("/product/{products_id}", status_code=status.HTTP_200_OK)
# async def read_data(products_id : int):
#     for product in PRODUCTS:
#         if product["id"] == products_id:
#             return product


# POST REQUEST
# CREATE AND INSERT DATA
# @app.post("/product/{product_id}")
# async def creat_data(new_product : dict):
#     PRODUCTS.append(new_product)
#     return {"status" : "created", "new_product" : new_product}

# PUT REQUEST
# UPDATE COMPLETE DATA
# @app.put("/product/{product_id}")
# async def update_data(product_id : int, new_updated_data : dict):
#     for index, product in enumerate(PRODUCTS):
#         if product["id"] == product_id:
#             PRODUCTS[index] = new_updated_data
#             return {"Status" : "Updated", "Product_id" : product_id, "New_updated_id" : new_updated_data}
        
# PATCH REQUEST
# UPDATE PARTIAL DATA
# @app.patch("/product/{product_id}")
# async def partial_data(product_id : int, new_updated_data : dict):
#     for product in PRODUCTS :
#         if product["id"] == product_id:
#             product.update(new_updated_data)
#             return {"Status" : "Partial Updates", "Product_id" : product_id, "new_updated_data" : product}

# DELETE REQUEST
# DELETE DATA
# @app.delete("/product/{product_id}")
# async def delete_data(product_id : int):
#     for index, product in enumerate(PRODUCTS) :
#         if product["id"] == product_id:
#             PRODUCTS.pop(index)
#             return {"status" : "Deleted", "product_id" : product_id}

# ****************************** QUERY PARAMETER VALIDATION *******************************
# PRODUCTS = [
#     {
#         "id" : 1,
#         "title" : "Ravan Backpack",
#         "price" : 109.84,
#         "discription" : "Perfect for everyday use and forest walk"
#     },
#     {
#         "id" : 2,
#         "title" : "Slim Fir T-Shirt",
#         "price" : 22.3,
#         "discription" : "Comfortable, Slim Fitting Casual Shirt"
#     },
#     {
#         "id" : 3,
#         "title" : "Cotton Jacket",
#         "price" : 59.9,
#         "discription" : "Great for outdoor activities and gifting"
#     }
# ]

# @app.get("/product")
# async def get_data(search : str | None = None):
#     if search:
#         search_lower = search.lower()
#         filtered_product = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_product.append(product)
#         return filtered_product
#     return PRODUCTS 

# VALIDATION WITHOUT ANNOTATED
# @app.get("/product")
# async def get_data(search : str | None = Query(default=None, max_length=5)):
#     if search:
#         search_lower = search.lower()
#         filtered_product = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_product.append(product)
#         return filtered_product
#     return PRODUCTS 

# VALIDATIONN WITH ANNOTATED
# @app.get("/product")
# async def get_data(
#     search :
#       Annotated[
#           str | None,
#             Query(max_length=5, pattern="^[a-z]+$")
#             ] = None):
#     if search:
#         search_lower = search.lower()
#         filtered_product = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_product.append(product)
#         return filtered_product
#     return PRODUCTS 
# # Why use Annotated
## CLEAR SEPERATION OF THE TYPE
## BETTER SUPPORT IN SOME EDITORS AND TOOLSFOR SHOWING METADATA AND VALIDATIONS DIRECTLY IN THE TYPE HINTS.
## REQUIRES PYTHON 3.9+ AND FASTAPI 0.95+; MORE MODERN AND RECOMMENDED APPROACH
## FASTAPI 0.95+ OFFICIALY RECOMMENDS USING ANNOTATED AND FOR DEPENDENCIES AND PARAMETERS.


# MULTIPLE SEARCH TERM (LIST)
# @app.get("/product")
# async def search_term(search : Annotated[list[str] | None, Query(alias="q")] = None): #using alias
#     if search:
#         filtered_product = []
#         for product in PRODUCTS:
#             for s in search:
#                 if s.lower() in product["title"].lower():
#                     filtered_product.append(product)
#         return filtered_product
#     return PRODUCTS

# ADDING METADATA
# @app.get("/products")
# async def get_products(search : Annotated[str | None, Query(alias="q", title="Search Product", description="Search by product title")]):
#     if search:
#         search_lower = search.lower()
#         filtered_products = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_products.append(product)
#         return filtered_products
#     return PRODUCTS        

# # DEPREATING PARAMETER
# @app.get("/product")
# async def get_product(search : Annotated[
#     str | None,
#     Query(deprecated=True)
# ] = None
# ):
#     if search:
#         search_lower = search.lower()
#         filtered_product = []
#         for product in PRODUCTS:
#             if search_lower in product["title"].lower():
#                 filtered_product.append(product)
#         return filtered_product
#     return PRODUCTS


# CUSTOM VALIDATION
# def check_valid_id(id : str):
#     if not id.startswith("prod-"):
#         raise ValueError("ID must be start from prob-")
#     return id

# @app.get("/product")
# async def get_product(id : Annotated[str | None, AfterValidator(check_valid_id)]=None):
#     if id :
#         return {"id" : id, "message" : "valid product ID"}
#     return {"message" : "No ID provided"}



# ************************ PATH PARAMETER VALIDATION ****************************
PRODUCTS = [
    {
        "id" : 1,
        "title" : "Ravan Backpack",
        "price" : 109.84,
        "discription" : "Perfect for everyday use and forest walk"
    },
    {
        "id" : 2,
        "title" : "Slim Fir T-Shirt",
        "price" : 22.3,
        "discription" : "Comfortable, Slim Fitting Casual Shirt"
    },
    {
        "id" : 3,
        "title" : "Cotton Jacket",
        "price" : 59.9,
        "discription" : "Great for outdoor activities and gifting"
    }
]
# BASIC PATH PARAMETER
# @app.get("/product/{product_id}")
# async def get_product(product_id : int):
#     for product in PRODUCTS :
#         if product["id"] == product_id:
#             return product
#         return {"error" : "Product not found"}
    
# NUMERIC PATH PARAMETER
# @app.get("/product/{product_id}")
# async def get_product(product_id : Annotated[int, Path(ge=1, le=3)]):
#     for product in PRODUCTS:
#         if product["id"] == product_id:
#             return product
#     return {"error" : "Product not found"}

# ADDING METADATA IN PATH PARAMETER
# @app.get("/product/{product_id}")
# async def get_product(product_id : Annotated[int, Path(title="The ID of the Product", description="This is product ID")]):
#     for product in PRODUCTS:
#         if product["id"] == product_id:
#             return product
#     return {"error" : "Product not found"}

# COMBINING PATH AND QUERY PARAMETER
@app.get("/product/{product_id}")
async def get_product(product_id : Annotated[int, Path(gt=0, le=100)],
                    search : Annotated[str | None, Query(max_length=20)]= None
                    ):
    for product in PRODUCTS:
        if product["id"] == product_id:
            if search in search.lower() not in product["title"].lower():
                return {"error" : "Product does not mat search term"}
            return product
    return {"error" : "Product not found"}