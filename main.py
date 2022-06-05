from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

# The Request order matters
# Example: Request GET method URL: "/"


# Path Operation or Route
@app.get("/")   # Decorator: We get the HTTP method and ("") path
def root():     # Function Will go to consist all the logic for performing the specific task

    return {"message": "Welcome to my API"}   # FastAPI will automatically converter the dictionary to a JSON format


@app.get("/posts")
def get_posts():

    return {"data": "This is your posts"}


@app.post("/createposts")
def create_posts(payload: dict = Body(...)):    # Extracts all of the fields from the body and convert to dictionary
    print(payload)
    return {"New Post": f"Title: {payload['title']} content: {payload['content']}"}

