from fastapi import FastAPI
from contextlib import asynccontextmanager

from todo_api.database import get_db
from routers import users, todos

@asynccontextmanager
async def lifespan(app: FastAPI):

    try:
        db = get_db()

        await db.command("ping")

        print("connected to MongoDB")

    except Exception as e:
        print("MongoDB connection failed")
        print(e)

    yield

app = FastAPI(lifespan=lifespan,
              title="TODO API",
              description="""
              A REST API with FastAPI anda MongoDB.
              
              Features
              - User Registration
              - JWT Authentication
              - TODO CRUD
              - Protected Routes
              """,
              version="1.0.0",)

app.include_router(users.router)
app.include_router(todos.router)

@app.get("/")
async def root():
    return {"message": "TODO API is running"}