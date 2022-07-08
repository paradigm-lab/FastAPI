from pydantic import BaseSettings


# Performing Validation for the Environment variables
class Settings(BaseSettings):   # Pydantic is going to handle the case sensitive
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int


settings = Settings()   # Creating an instance of the Settings() class
