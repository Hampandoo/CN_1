from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  PROJECT_NAME: str = "Gateway"
  PROJECT_VERSION: str = "0.1.0"
  secret_key: str = "testkey"
  SERVICE_1_URL: str = "http://localhost:8002/api/v1"
  SERVICE_2_URL: str = "http://localhost:8001/api/v1"
  GATEWAY_PORT: int = 8000

  class Config:
    env_file = ".env"

settings = Settings()