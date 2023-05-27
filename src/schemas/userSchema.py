from datetime import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    firstname: str
    lastname: str
    email: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    pass


class User(UserBase):
    id: str
    password_set: bool
    rights: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
