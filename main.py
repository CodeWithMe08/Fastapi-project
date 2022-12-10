from fastapi import FastAPI
from fastapi.params import Body


app = FastAPI()


@app.get("/")
def root():
    return {"message":"heelo world"}

@app.get("/posts")
def get_posts():
    return {"data":"posts"}

@app.post("/createposts")
def create_posts(payload: dict = Body(...)):
    print(payload)
    return {"new_post":f"title {payload['title']} content {payload['contetn']}"}

    
