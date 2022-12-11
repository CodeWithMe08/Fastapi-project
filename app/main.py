from fastapi import FastAPI, HTTPException, Response, status, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import psycopg2
from psycopg2.extras import RealDictCursor
from . import models
from .database import engine, get_db
from .routers import post, user, auth
import time 

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

while True:
    try:
        conn = psycopg2.connect(host="localhost", database="fastapi-project", user="postgres",
        password="sm7wx98d6kbi8", cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("database connection was successful")
        break
    except Exception as error:
        print("connecting to dataabsse failed")
        print("Error: ",error)
        time.sleep(5)

@app.get("/")
def root():
    return {"message":"heelo world"}
