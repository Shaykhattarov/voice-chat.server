import secrets

from typing import (
    Any, 
    Optional,
    List,
    Literal,
    Annotated
)

from pydantic import (
    AnyUrl,
    BeforeValidator,
    computed_field
)

from pydantic_settings import BaseSettings, SettingsConfigDict


def parse_cors(v: Any) -> list[str] | str:
    if isinstance(v, str) and not v.startswith("["):
        return [i.strip() for i in v.split(",")]
    elif isinstance(v, list | str):
        return v
    raise ValueError(v)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="../../.env", 
        env_ignore_empty=True,
        extra="ignore"
    )

    API_REST_STR: str = "/api/rest"
    API_WEBSOCKET_STR: str = "/api/websocket"
    SECRET_KEY: str = secrets.token_urlsafe(32)

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ENVIRONMENT: Literal['local', 'staging', 'production'] = 'local'

    BACKEND_CORS_ORIGIN: Annotated[List[AnyUrl], BeforeValidator(parse_cors)] = [
        "http://localhost",
        "http://127.0.0.1"
    ]

    @computed_field
    @property
    def all_cors_origin(self) -> List[str]:
        return [str(origin).rstrip("/") for origin in self.BACKEND_CORS_ORIGIN]


settings = Settings()