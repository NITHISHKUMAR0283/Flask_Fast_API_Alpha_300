from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title:str
    content:str
    like : bool =True
    rating :Optional[int]=None


my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "favorite foods", "content": "I like pizza", "id": 2}
]
@app.get("/")
def root():
    return {"message":"Hello world"}

@app.get("/post")
def getpost():
    return my_posts

@app.post("/postuser")
def post(payload:Post):
    print(payload)
    print(payload.dict())
    return f'{payload.title} and {payload.content}'