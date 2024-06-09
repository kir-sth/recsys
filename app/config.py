from pydantic_settings import BaseSettings, SettingsConfigDict

 
class Settings(BaseSettings):
    FASTAPI_HOST: str
    FASTAPI_PORT: int
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_NAME: str
    POSTGRES_DRIVER: str
    POSTGRES_URL: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
