import random
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}
@app.get("/test1")
async def read_root():
    return {"teste": True, "num_aleatorio": random.randint(0, 1000)}
