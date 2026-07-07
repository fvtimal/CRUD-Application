from fastapi import APIRouter, HTTPException, status

from database import users
from models import UserRegister

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: UserRegister):

    existing_user = await users.find_one(
        {"email": user.email}
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered."
        )

    user_dict = user.model_dump()

    await users.insert_one(user_dict)

    return {
        "message": "User Registered Successfully"
    }