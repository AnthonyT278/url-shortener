from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings, loaded from environment variables (or a .env file)."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # App
    app_name: str = "url-shortener"
    debug: bool = False

    # Database (SQLite by default for local development)
    database_url: str = "sqlite+aiosqlite:///./url_shortener.db"

    # Redis (used for caching click counts)
    redis_url: str = "redis://localhost:6379/0"

    # Auth / JWT
    secret_key: str = "change-me-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30


settings = Settings()

