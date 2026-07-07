#pydantc models

from pydantic import BaseModel, EmailStr


class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str



class TodoCreate(BaseModel):
    title: str
    completed: bool = False