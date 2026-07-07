from fastapi import APIRouter, Depends, HTTPException, status
from bson import ObjectId

from database import todos_collection
from models import TodoCreate
from dependencies import get_current_user

router = APIRouter(
    prefix="/todos",
    tags=["Todos"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_todo(
    todo: TodoCreate,
    current_user=Depends(get_current_user)
):

    todo_dict = todo.model_dump()

    todo_dict["owner_id"] = str(current_user["_id"])

    result = await todos_collection.insert_one(todo_dict)

    return {
        "message": "Todo created",
        "id": str(result.inserted_id)
    }
@router.get("/")
async def get_todos(
    current_user=Depends(get_current_user)
):

    todos = await todos_collection.find(
        {
            "owner_id": str(current_user["_id"])
        }
    ).to_list(length=None)

    formatted_todos = []

    for todo in todos:
        formatted_todos.append(
            {
                "id": str(todo["_id"]),
                "title": todo["title"],
                "completed": todo["completed"]
            }
        )

    return formatted_todos



@router.get("/{id}")
async def get_todo(
    id: str,
    current_user=Depends(get_current_user)
):

    todo = await todos_collection.find_one(
        {
            "_id": ObjectId(id),
            "owner_id": str(current_user["_id"])
        }
    )

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "completed": todo["completed"]
    }


@router.put("/{id}")
async def update_todo(
    id: str,
    todo: TodoCreate,
    current_user=Depends(get_current_user)
):

    result = await todos_collection.update_one(
        {
            "_id": ObjectId(id),
            "owner_id": str(current_user["_id"])
        },
        {
            "$set": todo.model_dump()
        }
    )

    if result.matched_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return {
        "message": "Todo updated successfully"
    }


@router.delete("/{id}")
async def delete_todo(
    id: str,
    current_user=Depends(get_current_user)
):

    result = await todos_collection.delete_one(
        {
            "_id": ObjectId(id),
            "owner_id": str(current_user["_id"])
        }
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return {
        "message": "Todo deleted successfully"
    }