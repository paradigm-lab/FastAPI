from fastapi import FastAPI

app = FastAPI() 


@app.get("/")
def index():

    return {"data": {"name": "User1"}}


@app.get("/about")
def about():
    return {"data": "About Page"}