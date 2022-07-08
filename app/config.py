from pydantic import BaseSettings


class Settings(BaseSettings):
    path: str
    language: str
    shell: str


settings = Settings()
