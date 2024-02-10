from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from random import  randrange

app = FastAPI()


# Schema for create a post
class Posts(BaseModel):
    # mandatory fields
    title: str
    content: str

    # optional fields
    status: bool = True
    active: Optional[int] = None


all_posts = [{"id": 1, "title": "Post 1", "content": "Post One is here"},
             {"id": 2, "title": "Post 2", "content": "Post Two is here"}]


@app.get("/posts")
def get_post():
    return {"data": all_posts}


@app.post("/posts")
def create_post(payload: Posts):
    print(payload)
    print(payload.dict())
    all_posts.append({"id": randrange(3,100), **payload.dict()})
    return {"data": payload.dict()}
