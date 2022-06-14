from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

# Top Down path request
app = FastAPI()


# Pydatic Model
# Schema
class Post(BaseModel):
    title: str
    content: str
    published: bool = True


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


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):    # Extracts all of the fields from the body and convert to dictionary
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


# Path parameter(id)
@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message": f"Post with id: {id} was not found"}
    return {"Post_detail": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    # Deleting post
    # Find the index in the array that has required ID
    # my_posts.pop(index)
    index = find_index_post(id)

    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} does not exist")

    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)

    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id: {id} does not exist")

    post_dict = post.dict()
    post_dict["id"] = id
    my_posts[index] = post_dict

    return {"data": post_dict}



