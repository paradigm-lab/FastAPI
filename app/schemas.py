from pydantic import BaseModel


# Extending Pydatic Model
# Schema
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


# Using Inheritance approach
class PostCreate(PostBase):
    pass
