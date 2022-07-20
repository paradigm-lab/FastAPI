import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.database import get_db, Base
from alembic import command
from app.oauth2 import create_access_token
from app import models
from app import main
# from app.main import app


# This is a special file that pytest use's and it allows as to define fixtures,
# Whereby all the fixture will be accessible in the test package (So it's package specific and sub-package)


# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:fastapi:fastapi@127.0.0.1:5432/fastapi_test"
SQLALCHEMY_DATABASE_URL = f'postgresql://' \
                          f'{settings.database_username}:' \
                          f'{settings.database_password}@' \
                          f'{settings.database_hostname}:' \
                          f'{settings.database_port}/' \
                          f'{settings.database_name}_test'

# The engine is responsible for establishing a connection
engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def session():
    # This logic will help in troubleshooting
    Base.metadata.drop_all(bind=engine)    # This will tell sqlalchemy to all of our tables
    # We can run our code before we run our test
    Base.metadata.create_all(bind=engine)  # This will tell sqlalchemy to create all of our tables
    # command.upgrade("head")       # Using alembic in testing
    # command.downgrade("base")
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


# Gives us unauthenticated client
@pytest.fixture(scope="function")
def client(session):        # client depends on session
    # yield TestClient(app)   # yield is the same as return
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    main.app.dependency_overrides[get_db] = override_get_db
    yield TestClient(main.app)


@pytest.fixture(scope="function")
def test_user(client):
    user_data = {"email": "developer@fastapi.com", "password": "developer"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user_data["password"]
    # print(res.json)
    return new_user


@pytest.fixture(scope="function")
def test_user2(client):
    user_data = {"email": "developer1@fastapi.com", "password": "developer"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user_data["password"]
    # print(res.json)
    return new_user


@pytest.fixture(scope="function")
def token(test_user):
    return create_access_token({"user_id": test_user["id"]})


# This fixture will give us an authenticated client
@pytest.fixture(scope="function")
def authorized_client(client, token):
    client.headers = {
        **client.headers,
        "Authorization": f"Bearer {token}"
    }

    return client


@pytest.fixture(scope="function")
def test_posts(test_user, session, test_user2):
    posts_data = [
        {
            "title": "First Title",
            "content": "First Content",
            "owner_id": test_user["id"]
        },
        {
            "title": "Second Title",
            "content": "Second Content",
            "owner_id": test_user["id"]
        },
        {
            "title": "Third Title",
            "content": "Third Content",
            "owner_id": test_user["id"]
        },
        {
            "title": "Fourth Title",
            "content": "Fourth Content",
            "owner_id": test_user2["id"]
        },
        {
            "title": "Fifth Title",
            "content": "Fifth Content",
            "owner_id": test_user2["id"]
        }
    ]

    def create_post_model(post):
        return models.Post(**post)

    post_map = map(create_post_model, posts_data)

    posts = list(post_map)

    session.add_all(posts)

    """
    session.add_all([
            models.Post(title="First Title", content="First Content", owner_id=test_user["id"]),
            models.Post(title="First Title", content="First Content", owner_id=test_user["id"]),
            models.Post(title="First Title", content="First Content", owner_id=test_user["id"])
    ])
    """

    session.commit()
    posts = session.query(models.Post).all()
    return posts




