from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title:str
    content:str

@app.get("/")
def root():
    return {"message":"Hello world"}

@app.post("/postuser")
def post(payload:Post):
    print(payload)
    return f'{payload.title} and {payload.content}'