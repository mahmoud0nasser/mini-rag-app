from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str
    
    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int  # in MB
    FILE_DEFAULT_CHUNK_SIZE: int  # in KB

    MONGODB_URL: str
    MONGODB_DATABASE: str

    class Config:
        env_file = ".env"

def get_settings():
    return Settings()
