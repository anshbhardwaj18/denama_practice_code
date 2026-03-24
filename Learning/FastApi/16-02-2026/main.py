from fastapi import FastAPI

app = FastAPI()
# Read or fetch all data
@app.get("/product")
async def all_product():
    return {"response" : "All Product"}

# Read or fetch single data
@app.get("/product/{product_id}")
async def all_product(product_id):
    return {"response" : "Single Data Fetched", "product id": product_id}