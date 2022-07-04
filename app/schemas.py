from pydantic import BaseModel, EmailStr
from datetime import datetime


# Pydatic Model Extend BaseModel
# Schema
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


# Using Inheritance approach
class PostCreate(PostBase):
    pass


# Response schema
class Post(PostBase):   # Inherit the PostBase
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

