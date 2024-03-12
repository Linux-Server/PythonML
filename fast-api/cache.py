from fastapi import FastAPI
from redis import Redis
import requests
import json
from contextlib import asynccontextmanager

redis_connection = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the redis - Startup
    redis_connection["redis"] = Redis(host="localhost", port=6379)
    yield
    # Close Redis - Shutdown
    redis_connection.clear()

app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    try:
        value = redis_connection["redis"].get("entries")
        if value is None:
            response = requests.get("https://api.publicapis.org/entries")# 1800 -2000 ms
            response= response.json()
            value = json.dumps(response)
            redis_connection["redis"].set("entries", value)
        return {"message": value}

    except Exception as e:
        print("Error : ", e)


@app.get("/check")
async def tester():
    data = await requests.get("https://api.publicapis.org/entries")
    print(data)
    return {"message": "Async Test"}
