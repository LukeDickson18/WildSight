from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int

    jwt_secret_key: str = "change-this-secret-before-production"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    cors_origins: list[str] = Field(
        default_factory=lambda: [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        ]
    )

    open_meteo_archive_url: str = (
        "https://archive-api.open-meteo.com/v1/archive"
    )

    open_meteo_forecast_url: str = (
        "https://api.open-meteo.com/v1/forecast"
    )
    
    open_meteo_timeout: int = 20

    hotspot_link_distance_m: int = 1000
    # ebird_api_key: str
    # ebird_base_url: str = ...
    # inaturalist_base_url: str = ...
    # opentopodata_base_url: str = ...

    model_config = SettingsConfigDict(
        case_sensitive=False,
    )

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg://"
            f"{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}"
            f"/{self.postgres_db}"
        )


settings = Settings()