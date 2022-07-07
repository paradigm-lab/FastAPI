from fastapi.params import Body
from random import randrange

from fastapi import FastAPI, Response, status, HTTPException, Depends
from . import models, schemas, utils
from .database import engine
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)

# Top Down path request
app = FastAPI()


my_posts = [
    {"title": "Title of post 1", "content": "content of post 1", "id": 1},
    {"title": "Favorite foods", "content": "I like pizza", "id": 2}
]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i


# The Request order matters
# Example: Request GET method URL: "/"

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


# Path Operation or Route
@app.get("/")  # Decorator: We get the HTTP method and ("") path
def root():  # Function Will go to consist all the logic for performing the specific task

    return {"message": "Welcome to my API"}  # FastAPI will automatically converter the dictionary to a JSON format



'''
@app.post("/createposts")
def create_posts(payload: dict = Body(...)):    # Extracts all of the fields from the body and convert to dictionary
    print(payload)
    return {"New Post": f"Title: {payload['title']} content: {payload['content']}"}
'''




