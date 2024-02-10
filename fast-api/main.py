from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Schema for create a post
class Posts(BaseModel):
    # mandatory fields
    title:str
    content:str
    
    #optional fields
    status:bool = True
    active:Optional[int] = None
    

@app.get("/")
def root():
    return {"message" : "FAst api generated"}


@app.get("/posts")
def get_post():
    return {"message": "All post fetched"}

@app.post("/posts")
def create_post(payload: Posts):
    print(payload)
    print(payload.title)
    return {"message": "Post Created!"}


