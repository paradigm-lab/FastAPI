import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.config import settings
from app.database import get_db, Base
from alembic import command


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


@pytest.fixture(scope="module")
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


@pytest.fixture(scope="module")
def client(session):        # client depends on session
    # yield TestClient(app)   # yield is the same as return
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
