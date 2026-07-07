from fastapi import APIRouter, HTTPException, status

from database import users
from models import UserRegister
from security import hash_password


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserRegister):

    existing_user = await users.find_one(
        {
            "email": user.email
        }
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )


    hashed_password = hash_password(
        user.password
    )


    user_dict = user.model_dump()


    user_dict["password"] = hashed_password


    await users.insert_one(
        user_dict
    )


    return {
        "message": "User Registered Successfully"
    }