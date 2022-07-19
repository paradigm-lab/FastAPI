from app import schemas
from .database import session, client


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


def test_login_user(client):
    res = client.post("/login", data={"username": "developer@fastapi.com", "password": "developer"})
    print(res.json())
    assert res.status_code == 200
