from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    REDIS_HOST: str = 'localhost'
    REDIS_PORT: int = 6379

@lru_cache
def get_settings():
    return Settings()