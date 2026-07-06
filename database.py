from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient("mongodb://localhost:27017")
#connecting to mongodb

db = client.todo_db
#connecting to db

#collections---
users = db.users
todos = db.todos


