from fastapi import FastAPI
from database import db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await db.command("ping")
        print("connected to MongoDB")
    except Exception as e:
        print("MongoDB connection failed")
        print(e)

    yield
    

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return {"message": "TODO API is running"}