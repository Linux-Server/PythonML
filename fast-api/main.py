from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange
import psycopg

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


def find_post(id: int):
    for i in all_posts:
        if i["id"] == id:
            return i


@app.get("/posts")
def get_posts():
    return {"data": all_posts}


@app.get("/posts/latest")
def get_latest_post():
    print("Inside out")
    return all_posts[len(all_posts) - 1]


# fetch individual post
@app.get("/posts/{id}")
def get_post(id: int, ):
    print(id)
    return_data = find_post(id)
    if not return_data:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data Not Found!")
    return {"message": return_data}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(payload: Posts):
    print(payload)
    print(payload.dict())
    all_posts.append({"id": randrange(3, 100), **payload.dict()})
    return {"data": payload.dict()}

def find_by_id(id):
    for i,p in enumerate(all_posts):
        if p["id"] == id:
            return i


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    return_id = find_by_id(id)
    if return_id == None:
        raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No data found to be deleted")
    all_posts.pop(return_id)
    raise HTTPException(status_code=204, detail="Post deleted Successfully")


@app.put("/posts/{id}")
def update_post(id:int, payload:Posts):
    return_id = find_by_id(id)
    if return_id ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Update data not found")
    payload_dict = payload.dict()
    payload_dict["id"] = id
    print("Payload is : ", payload_dict)
    all_posts[return_id] = payload_dict
    return "Post udated success"