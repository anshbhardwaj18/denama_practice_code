from fastapi import FastAPI

app = FastAPI()
# GET REUQEST
# READ AND FETCH ALL DATA
@app.get("/product")
async def all_prodct():
    return {"response" : "All Product"}

# READ AND FETCH ALL DATA
@app.get("/product/{product_id}")
async def single_product(product_id:int):
    return {"response": "Single data fetched", "product_id" : product_id}

# POST REQUEST
# CREATE AND INSERT DATA
@app.post("/product")
async def create_product(new_product : dict):
    return {"response": "Product created", "new product" : new_product}

# PUT REQUEST
# UPDATE COMPLETE DATA
@app.put("/product/{product_id}")
async def update_product(update_product : dict, product_id : int):
    return {"response" : "Product Update", "Product id" : product_id ,"Update Product" : update_product}

# PATCH REQUEST
# PARTIAL UPDATE
@app.patch("/product/{product_id}")
async def partial_update_product(partial_update : dict, product_id : int):
    return {"response" : "Product update", "Product id" : product_id, "Partial Product":
            partial_update}

# DELETE REQUEST
# DELETE DATA
@app.delete("/product/{product_id}")
async def delete_product(product_id : int):
    return {"response" : "Product delete sucessfully", "Product id" : product_id}
