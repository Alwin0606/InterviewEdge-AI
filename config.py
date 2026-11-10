
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "InterviewEdge AI"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "AI-powered adaptive technical interview platform"
    API_PREFIX: str = "/api/v1"

    SECRET_KEY: str = "change-this-to-a-secure-secret-key"

    DATABASE_URL: str = "postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/interviewedge"

    OPENAI_API_KEY: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()
