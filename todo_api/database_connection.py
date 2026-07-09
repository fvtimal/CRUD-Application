from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient


_async_client = None
_sync_client = None


mongo_uri = "mongodb://localhost:27017"


def get_database(database="todo_db", force_async=True):

    global _async_client
    global _sync_client

    if force_async:

        if _async_client is None:
            _async_client = AsyncIOMotorClient(mongo_uri)
            print("Successfully connected to MongoDB (async mode)!")

        return _async_client[database]

    else:

        if _sync_client is None:
            _sync_client = MongoClient(mongo_uri)
            print("Successfully connected to MongoDB!")

        return _sync_client[database]