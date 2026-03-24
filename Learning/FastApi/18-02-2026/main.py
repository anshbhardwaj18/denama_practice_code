from fastapi import FastAPI
from enum import Enum

app = FastAPI()

#*************************** PATH PARAMTER WITH TYPE *********************
# WITHOUT TYPE :- DEFAULT STRING
# @app.get("/product/{product_id}")     
# async def single_product(product_id):
#     return {"response" : "Single data response", "Product id" : product_id}

# WITH TYPE :- TYPE - INT
# @app.get("/product/{product_id}")
# async def single_product(product_id:int):
#     return {"response" : "Single data response", "Product id" : product_id}

#*************************** PATH PARAMETER ORDERS MATTER **********************
# STATIC RESPONSE--------------->>>>>>>>>>
# @app.get("/product/specific response")
# async def single_product():
#     return {"Response" : "Single data response"}

# DYNAMIC RESPONSE--------------->>>>>>>>>>>
# @app.get("/product/{product_title}")
# async def dynamic_product(product_title : str):
#     return {"Response" : "Dynamic Response", "Product Title" : product_title}

#*************************** PATH PARAMETER PREEFINED VALUE **********************
# DEFINE AN ENUM CLASS WITH ALLOWED PRODUCT CATEGORY
# class ProductCategory(str, Enum):
#     books = "Books"
#     clothing = "Clothing"
#     electronics = "Electronics"

# USE THE ENUM AS THE TYPE FOR THE PATH PARAMETER
# @app.get("/product/{category}")
# async def get_product(category:ProductCategory):
#     return {"response" : "Product fetched", "Category" : category}

# WORKING WITH PYTHON ENUMERATION
# class ProductCategory(str, Enum):
#     books = "Books"
#     clothing = "Clothing"
#     electronics = "Electronics"

# @app.get("/product/{category}")
# async def get_product(category:ProductCategory):
#     if category == ProductCategory.books:
#         return {"category" : category, "Message" : "book was awesome"}
#     elif category.value == "Clothing":
#         return {"category" : category, "Message" : "Nice trending cloths"}
#     elif category == ProductCategory.electronics:
#         return {"Category" : category, "Message" : "Awesome Gadget"}
#     else:
#         return {"category" : category, "Message" : "Does't match"}


#************************* PATH CONVERTER ************************
# @app.get("/files/{file_path:path}")
# async def read_files(file_path:str):
#     return {"Your requested file at path " : file_path}

# ************************ USING THE ABOVE METHOD MAKE A CRUD OPERATION USING PATH PARAMETER********************

PRODUCTS = [
    {
        "id" : 1,
        "title" : "HP Omnibook 5 OLED, Snapdragon X Processor",
        "Price" : 109.85,
        "discription" : "Processor, Memory & Storage: Snapdragon X X1-26-100 (up to 2.97 GHz, 8 cores) | Memory: Snapdragon X X1-26-100 (up to 2.97 GHz, 8 cores) | Storage: 1 TB PCIe NVMe M.2 SSD"
    },
    {
        "id" : 2,
        "title" : "ASUS Vivobook Go 14, AMD Ryzen 3 7320U",
        "Price" : 200.89,
        "discription" : "Processor : AMD Ryzen 3 7320U Processor 2.4GHz (6MB Cache, up to 4.1GHz, 4 cores, 8 Threads) Display : 14.0-inch, FHD (1920 x 1080) 16:9 aspect ratio, 60Hz refresh rate, 250nits Brightness | Keyboard : Chiclet Keyboard"
    },
    {
        "id" : 3,
        "title" : "Dell 15, Intel Core 3, 14th Gen-100U, 8GB DDR4",
        "Price" : 100.95,
        "discription" : "Processor: Intel Core 3 100U 14th Generation (up to 4.70 GHz, 10MB 6 Cores)RAM & Storage: 8 GB, 1 x 8 GB, DDR4, 2666 MT/s & 512GB SSD Software: Pre-Loaded Windows 11 Home with Lifetime Validity | MS Office Home and Student 2024 with lifetime validity| McAfee Multi-Device Security 12-month subscription Graphics & Keyboard: Intel UHD Graphics & Standard Keyboard"
    },
]

# GET REQUEST
# READ AND FETCH ALL DATA
# ALL DATA FETCH
@app.get("/product")
async def read_data():
    return PRODUCTS

# SINGLE DATA FETCH
@app.get("/product/{products_id}")
async def read_data(products_id : int):
    for product in PRODUCTS:
        if product["id"] == products_id:
            return product


# POST REQUEST
# CREATE AND INSERT DATA
@app.post("/product")
async def creat_data(new_product : dict):
    PRODUCTS.append(new_product)
    return {"status" : "created", "new_product" : new_product}

# PUT REQUEST
# UPDATE COMPLETE DATA
@app.put("/product/{product_id}")
async def update_data(product_id : int, new_updated_data : dict):
    for index, product in enumerate(PRODUCTS):
        if product["id"] == product_id:
            PRODUCTS[index] = new_updated_data
            return {"Status" : "Updated", "Product_id" : product_id, "New_updated_id" : new_updated_data}
        
# PATCH REQUEST
# UPDATE PARTIAL DATA
@app.patch("/product/{product_id}")
async def partial_data(product_id : int, new_updated_data : dict):
    for product in PRODUCTS :
        if product["id"] == product_id:
            product.update(new_updated_data)
            return {"Status" : "Partial Updates", "Product_id" : product_id, "new_updated_data" : product}

# DELETE REQUEST
# DELETE DATA
@app.delete("/product/{product_id}")
async def delete_data(product_id : int):
    for index, product in enumerate(PRODUCTS) :
        if product["id"] == product_id:
            PRODUCTS.pop(index)
            return {"status" : "Deleted", "product_id" : product_id}