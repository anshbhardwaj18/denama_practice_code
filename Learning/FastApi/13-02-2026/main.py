from fastapi import FastAPI

app = FastAPI()

@app.get("/product")
async def all_product():
    return {"response" : "All Product"}