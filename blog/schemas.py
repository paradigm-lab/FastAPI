from pydantic import BaseModel


# Pydantic model
class Blog(BaseModel):
    title: str
    body: str

