from jose import JWTError, jwt
from datetime import datetime, timedelta

# SECRET_KEY
# Algorithm
# Expiration time

# To get a string like this run "openssl rand -hex 32"
SECRET_KEY = "6b02679b2bda59ee77826b19dfbeda795fa77715f27053834d25e73cbb154673"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    # Creating the copy of the data
    to_encode = data.copy()

    # Giving out the Expiration Time
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    # Passing the SECRET_KEY, Algorithm and Data
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)    # JWT Token Creation (payload)

    return encoded_jwt

