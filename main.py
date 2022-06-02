from fastapi import FastAPI

app = FastAPI()


# path ("/")
# get/put/post/delete is the operation
# path operation function
# @app is called path operation decorator
@app.get("/")
def index():

    return {"data": {"name": "User1"}}


@app.get("/about")
def about():
    return {"data": "About Page"}