from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  PROJECT_NAME: str = "Parser App"
  PROJECT_VERSION: str = "0.1.0"
  DATABASE_URL: str = 'sqlite:///parsersdb.db'
  secret_key: str = "testkey"
  PORT: int = 8001

  class Config:
    env_file = ".env"

settings = Settings()