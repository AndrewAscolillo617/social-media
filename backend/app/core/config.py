from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://placeholder"
    REDIS_URL: str = "redis://placeholder"
    SECRET_KEY: str = "placeholder"

    class Config:
        env_file = ".env"

settings = Settings()
