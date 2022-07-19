from jose import jwt
from app import schemas
from app.config import settings


def test_root(client):
    res = client.get("/")
    print(res.json().get("message"))
    assert res.json().get("message") == "Welcome to my API"
    assert res.status_code == 200


def test_create_user(client):
    res = client.post("/users/", json={"email": "developer@fastapi.com", "password": "developer"})
    new_user = schemas.UserOut(**res.json())  # Unpacking the dictionary
    assert new_user.email == "developer@fastapi.com"
    assert res.status_code == 201


def test_login_user(client, test_user):
    # Getting access to our login route
    res = client.post("/login", data={"username": test_user["email"], "password": test_user["password"]})
    login_res = schemas.Token(**res.json())

    # Decoding the token
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    user_id = payload.get("user_id")

    # Checking for validation for our user and the token
    assert user_id == test_user["id"]
    assert login_res.token_type == "bearer"
    assert res.status_code == 200


def test_incorrect_login(test_user, client):
    res = client.post("/login", data={"username": test_user["email"], "password": "Wrong Password"})
    assert res.status_code == 403
    assert res.json().get("detail") == "Invalid Credentials"
