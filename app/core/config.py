from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "Task Management API"
    environment: str = "development"
    database_url: str = "postgresql://postgre:postgre@localhost:5432/db"
    test_database_url: str = "postgresql://postgre:postgre@localhost:5432/test_db"
    secret_key: str = "my_secret_key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    redis_url: str = "redis://localhost:6379/0"
    celery_broker_url: str = "redis://localhost:6379/1"
    celery_result_backend: str = "redis://localhost:6379/2"

    model_config = SettingsConfigDict(env_file= ".env", env_file_encoding="utf-8")

settings = Settings()