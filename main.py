from typing import Optional

from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()


# Pydatic Model
class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
            {"title": "Title of post 1", "content": "content of post 1", "id": 1},
            {"title": "Favorite foods", "content": "I like pizza", "id": 2}
        ]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


# The Request order matters
# Example: Request GET method URL: "/"


# Path Operation or Route
@app.get("/")   # Decorator: We get the HTTP method and ("") path
def root():     # Function Will go to consist all the logic for performing the specific task

    return {"message": "Welcome to my API"}   # FastAPI will automatically converter the dictionary to a JSON format


@app.get("/posts")
def get_posts():

    return {"data": my_posts}   # FastAPI is going to serialize into JSON


'''
@app.post("/createposts")
def create_posts(payload: dict = Body(...)):    # Extracts all of the fields from the body and convert to dictionary
    print(payload)
    return {"New Post": f"Title: {payload['title']} content: {payload['content']}"}
'''


@app.post("/posts")
def create_posts(post: Post):    # Extracts all of the fields from the body and convert to dictionary
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


# Path parameter(id)
@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    return {"Post_detail": post}





