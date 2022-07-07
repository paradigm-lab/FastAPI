from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas, database, models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

outh2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# SECRET_KEY
# Algorithm
# Expiration time

# To get a string like this run "openssl rand -hex 32"
SECRET_KEY = "6b02679b2bda59ee77826b19dfbeda795fa77715f27053834d25e73cbb154673"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60        # Expiration token should only be withing 30 MINUTES


def create_access_token(data: dict):
    # Creating the copy of the data
    to_encode = data.copy()

    # Giving out the Expiration Time
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    # Passing the SECRET_KEY, Algorithm and Data
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)    # JWT Token Creation (payload)

    return encoded_jwt


def verify_access_token(token: str, credentials_exception):

    try:
        # Extracting the data
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)
    except JWTError as e:
        print(e)
        raise credentials_exception
    except AssertionError as e:
        print(e)

    return token_data   # id


def get_current_user(token: str = Depends(outh2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f"Could not validate credentials",
                                          headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token, credentials_exception)

    user = db.query(models.User).filter(models.User.id == token.id).first()

    return user

