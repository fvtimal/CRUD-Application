from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from todo_api.database import users
from todo_api.models import UserRegister
from todo_api.security import hash_password, verify_password
from routers.auth import create_access_token
from todo_api.dependencies import get_current_user


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
async def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):

    existing_user = await users.find_one(
        {
            "email": form_data.username
        }
    )

    if not existing_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    password_correct = verify_password(
        form_data.password,
        existing_user["password"]
    )

    if not password_correct:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        {
            "user_id": str(existing_user["_id"])
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

@router.get("/me")
async def get_profile(
    current_user = Depends(get_current_user)
):

    return {
        "id": str(current_user["_id"]),
        "username": current_user["username"],
        "email": current_user["email"]
    }