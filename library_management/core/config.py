from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict
from starlette.config import Config

BASE_DIR = Path(__file__).parent.parent

config = Config(".env")


class RunConfig(BaseModel):
    host: str = "localhost"
    port: int = 8000


class DatabaseConfig(BaseModel):
    DB_ENGINE: str = config("DB_ENGINE")
    DB_USER: str = config("DB_USER")
    DB_PASSWORD: str = config("DB_PASSWORD")
    DB_HOST: str = config("DB_HOST")
    DB_PORT: str = config("DB_PORT")
    DB_NAME: str = config("DB_NAME")
    url: str = f"{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    echo: bool = bool(int(config("DB_ECHO")))
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra="ignore")
    run: RunConfig = RunConfig()
    db: DatabaseConfig = DatabaseConfig()


settings = Settings()