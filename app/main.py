from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote

# models.Base.metadata.create_all(bind=engine) # This will tell sqlalchemy to create the tables in the db

# Top Down path request
app = FastAPI()

# The Request order matters
# Example: Request GET method URL: "/"

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


# Path Operation or Route
@app.get("/")  # Decorator: We get the HTTP method and ("") path
def root():  # Function Will go to consist all the logic for performing the specific task

    return {"message": "Welcome to my API"}  # FastAPI will automatically converter the dictionary to a JSON format

