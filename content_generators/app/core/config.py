from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  PROJECT_NAME: str = "Generator App"
  PROJECT_VERSION: str = "0.1.0"
  DATABASE_URL: str = 'sqlite:///generatorsdb.db'
  secret_key: str = "testkey"

  class Config:
    env_file = ".env"

settings = Settings()