#pydantc models

from pydantic import BaseModel, EmailStr, Field


class UserRegister(BaseModel):
    username: str = Field(
        example="John"
    )
    email: EmailStr = Field(
        example="john@gmail.com"
    )
    password: str = Field(
        example="password123"
    )



class TodoCreate(BaseModel):
    title: str = Field(
        example="Study FastAPI"
    )

    completed: bool = False


class TodoResponse(BaseModel):
    id: str
    title: str
    completed: bool