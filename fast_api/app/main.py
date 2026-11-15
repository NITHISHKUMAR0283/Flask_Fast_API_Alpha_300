from fastapi import FastAPI,Response,status,HTTPException,Depends
from fastapi.params import Body
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
# from random import randint
# import psycopg2
# from psycopg2.extras import RealDictCursor
import time
from . import model
from .database import engine, get_db


model.Base.metadata.create_all(bind=engine)

app = FastAPI()


# while True:
#     try:
#         conn = psycopg2.connect(host="localhost",database = "fastapi" , user = 'postgres' , password='ASNRangusumathi@2006',cursor_factory = RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful!")
#         break
#     except Exception as error:
#         print("connecting to database failed")
#         print("Error ",error)
#         time.sleep(2)

class Post(BaseModel):
    title:str
    content:str
    published : bool =True

@app.get("/")
def root():
    return {"message":"Hello world"}

@app.get("/post")
def getpost(db :Session = Depends(get_db)):
    post = db.query(model.Post).all()
    return post

@app.post("/postuser",status_code = status.HTTP_201_CREATED)
def post(payload:Post,db :Session = Depends(get_db)):

    new_post = model.Post(**payload.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data" : new_post}


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db :Session = Depends(get_db)):
    post_query = db.query(model.Post).filter(model.Post.id==id)
    
    if post_query==None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"post not found")
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.get("/postuser/{id}")
def get_post(id:int,response:Response,db :Session = Depends(get_db)):
    post = db.query(model.Post).filter(model.Post.id == id).first()

    if post==None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"post not found")
    return f'got the {id} , data : {post}'

@app.put("/posts/{id}")
def update_post(id: int, post: Post,db :Session = Depends(get_db)):


    post_query = db.query(model.Post).filter(model.Post.id==id)
    
    if post_query==None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"post not found")
    post_query.update(post.dict(),synchronize_session = False)
    db.commit()
    return {"data": post_query}