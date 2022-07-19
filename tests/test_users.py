import pytest
from jose import jwt
from app import schemas
from .database import session, client
from app.config import settings


@pytest.fixture(scope="function")
def test_user(client):
    user_data = {"email": "developer@fastapi.com", "password": "developer"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user_data["password"]
    # print(res.json)
    return new_user


def test_root(client):
    res = client.get("/")
    print(res.json().get("message"))
    assert res.json().get("message") == "Welcome to my API"
    assert res.status_code == 200


def test_create_user(client):
    res = client.post("/users/", json={"email": "developer@fastapi.com", "password": "developer"})
    new_user = schemas.UserOut(**res.json())    # Unpacking the dictionary
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
