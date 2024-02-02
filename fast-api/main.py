from fastapi import FastAPI
from pydantic import BaseModel
from random import randrange
from datetime import time
app = FastAPI()


class Post(BaseModel):
    title: str
    content: str


all_post = [{"id": 1, "title": "Post 1", "content": "Hello Post 1"}]


@app.get("/")
def root():
    return {"message": "Hello World Sachin"}


@app.post("/posts")
def create_post(payload: Post):
    new_post = {}   #payload.dict()
    new_post['id'] = randrange(2,10000000)
    new_post.update(payload)
    print(str(time.second))
    all_post.append(new_post)
    return {"message": f"New Post Created with title {payload.title} and it contain : {payload.content}"}


@app.get("/posts")
def get_post():
    return all_post
