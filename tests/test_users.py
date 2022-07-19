import pytest
from app import schemas
from .database import session, client


@pytest.fixture(scope="function")
def test_user(client):
    user_data = {"email": "developer@fastapi.com", "password": "developer"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user_data["password"]
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
    res = client.post("/login", data={"username": test_user["email"], "password": test_user["password"]})
    print(res.json())
    assert res.status_code == 200
