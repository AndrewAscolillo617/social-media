from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://placeholder"
    REDIS_URL: str = "redis://placeholder"
    SECRET_KEY: str = "placeholder"
    CORS_ORIGINS: list[str] = ["http://localhost:3000"]
    TRUSTED_HOSTS: list[str] = ["localhost", "127.0.0.1"]
    ENABLE_GZIP: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
