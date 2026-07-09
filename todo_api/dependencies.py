#current user dependency
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from bson import ObjectId

from todo_api.auth import SECRET_KEY, ALGORITHM
from todo_api.database import get_users


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/users/login"
)


async def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("user_id")

        if user_id is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )


    users = get_users()
    user = await users.find_one(
        {
            "_id": ObjectId(user_id)
        }
    )


    if user is None:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )


    return user