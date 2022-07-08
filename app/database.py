import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
from psycopg2.extras import RealDictCursor # Gives back the column name as well as the value (Return a python Dictionary)
import time

SQLALCHEMY_DATABASE_URL = f'postgresql://' \
                          f'{settings.database_username}:' \
                          f'{settings.database_password}@' \
                          f'{settings.database_hostname}:' \
                          f'{settings.database_port}/' \
                          f'{settings.database_name}'

# The engine is responsible for establishing a connection
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency to get a session to the database to send SQL statement
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""
# Postgres database driver for sending raw sql queries
while True:
    try:
        conn = psycopg2.connect(host="127.0.0.1", database="post", user="fastapi", password="fastapi",
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database Connection was successfully!")
        break
    except Exception as error:
        print("Connection to database failed")
        print("Error: ", error)
        time.sleep(2)
"""

