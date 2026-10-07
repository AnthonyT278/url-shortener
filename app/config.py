from pydantic_settings import BaseSettings 

class Settings(BaseSettings):
    database_url: str = "sqlite+aiosqlite:///./shortener.db"
    redis_url: str = "redis://localhost:6379"
    secret_key: str = "change-me-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24
    base_url: str = "http://localhost:8000"

settings = Settings()