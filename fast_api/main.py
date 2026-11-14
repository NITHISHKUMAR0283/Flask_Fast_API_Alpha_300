from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randint

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
    post_dict = payload.model_dump()
    post_dict['id'] = randint(0,100000000)
    my_posts.append(post_dict)
    return my_posts

@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}

@app.get("/postuser/{id}")
def getpost(id:int):
    return f'got the {id}'