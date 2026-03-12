from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    LASTFM_API_KEY: str
    BASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
