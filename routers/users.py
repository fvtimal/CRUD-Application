from fastapi import APIRouter, HTTPException, status

from database import users
from models import UserRegister, UserLogin
from security import hash_password
from security import verify_password
from routers.auth import create_access_token


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

@router.post("/login")
async def login(user: UserLogin):

    existing_user = await users.find_one(
        {
            "email": user.email
        }
    )


    if not existing_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )


    password_correct = verify_password(
        user.password,
        existing_user["password"]
    )


    if not password_correct:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )


    token = create_access_token(
        {
            "user_id": str(existing_user["_id"])
        }
    )


    return {
        "access_token": token,
        "token_type": "bearer"
    }