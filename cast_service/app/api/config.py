from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URI: str = "postgresql://postgres:123456@localhost/cast_db_dev"

settings = Settings()