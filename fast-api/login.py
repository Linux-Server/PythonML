from fastapi import FastAPI, Request
from redis import Redis
import requests
import json

app = FastAPI()


@app.on_event("startup")
async def start_event():
    app.state.redis = Redis(host="localhost", port=6379)


@app.on_event("shutdown")
async def shut_down():
    app.state.redis.close()


# To access header data
@app.get("/")
def login_user():
    value = app.state.redis.get("entries")
    if value is None:
        response = requests.get("https://api.publicapis.org/entries")
        response = response.json()
        value = response
        app.state.redis.set("entries", json.dumps(response))

    return {"message": value}
