from fastapi import FastAPI,Response,status,HTTPException
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

@app.post("/postuser",status_code = status.HTTP_201_CREATED)
def post(payload:Post):
    post_dict = payload.model_dump()
    post_dict['id'] = randint(0,100000000)
    my_posts.append(post_dict)
    return my_posts
def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)

    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} does not exist"
        )

    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}

@app.get("/postuser/{id}")
def get_post(id:int,response:Response):
    p = False
    if not p:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"post not found")
    return f'got the {id}'