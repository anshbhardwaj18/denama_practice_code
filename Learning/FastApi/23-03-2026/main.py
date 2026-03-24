from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {
    "apple" : "A juice fruit",
    "banana" : "A yellow color fruit"
}

@app.get("/items/{items_id}")
async def get_data(items_id: str):
    return items[items_id]