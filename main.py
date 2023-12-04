from fastapi import FastAPI
from utils import get_location, get_schools

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/data/{location}")
async def data_test(location: str):
    return get_location(location)


@app.get("/calc")
async def data_test(lat: float, lng: float):
    return get_schools(lat, lng)
