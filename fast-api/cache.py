from fastapi import FastAPI
from redis import Redis
import requests
import json
app = FastAPI()



@app.on_event("startup")
def start_up():
    app.state.redis = Redis(host="localhost", port=6379)

@app.on_event("shutdown")
def shut_down():
    app.state.redis.close()

@app.get("/")
def root():
    value = app.state.redis.get("entries")
    if value is None:
        response = requests.get("https://api.publicapis.org/entries")# 1800 -2000 ms
        response= response.json()
        value = json.dumps(response)
        app.state.redis.set("entries", value)



    return {"message": value}