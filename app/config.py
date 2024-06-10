from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    FASTAPI_HOST: str
    FASTAPI_PORT: int
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DRIVER: str
    POSTGRES_DB: str

    def postgres_url(self) -> str:
        return f"{self.POSTGRES_DRIVER}://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
print(settings.postgres_url())
