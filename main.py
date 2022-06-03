from fastapi import FastAPI
from typing import Optional

app = FastAPI()


# path ("/")
# get/put/post/delete is the operation
# path operation function
# @app is called path operation decorator
@app.get("/")
def index():
    return {"data": {"data": "Blog List"}}


# Query Parameter ? & Optional
@app.get("/blog")
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    # Only get 10 published blogs
    if published:
        return {"data": f"{limit} published blogs from the db"}
    else:
        return {"data": f"{limit} blogs from the db"}


@app.get("/blog/unpublished")
def unpublished():
    return {"data": "all unpublished blogs"}


# Dynamic routing
# The type definition is all done by Pydantic library
@app.get("/blog/{id}")
def show(id: int):
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id):
    # Fetch comments of blog with id = id
    return {"data": {"1", "2"}}

