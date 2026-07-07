from fastapi import FastAPI
from database import db
from contextlib import asynccontextmanager

from database import db
from routers import users, todos

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
app.include_router(users.router)
app.include_router(todos.router)

@app.get("/")
async def root():
    return {"message": "TODO API is running"}