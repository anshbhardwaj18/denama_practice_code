from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "Hello World"}

@app.get("/about")
async def name():
    return{"My name" : "Ansh bhardwaj"}

@app.get("/age")
async def age():
    return{"My age" : 21}

@app.get("/sum")
async def sum(a: int, b: int):
    return{"Sum" : a + b}

@app.get("/sub")
def sum(a:int, b: int):
    return{"Sub" : a - b}
