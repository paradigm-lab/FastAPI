import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.config import settings
from app.database import get_db, Base
from alembic import command


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


@pytest.fixture(scope="function")
def client(session):        # client depends on session
    # yield TestClient(app)   # yield is the same as return
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)


@pytest.fixture(scope="function")
def test_user(client):
    user_data = {"email": "developer@fastapi.com", "password": "developer"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    new_user = res.json()
    new_user["password"] = user_data["password"]
    # print(res.json)
    return new_user


