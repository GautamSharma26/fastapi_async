from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(find_dotenv())


class Settings(BaseSettings):
    """
        # https://pydantic-docs.helpmanual.io/usage/settings/
        Create a clearly-defined, type-hinted application configuration class
        Automatically read modifications to the configuration from environment variables
        Manually override specific settings in the initializer where desired (e.g. in unit tests)
    """
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    SQLALCHEMY_DATABASE_URL: str


class BaseAppConfig(object):
    """
    Set base configuration, env variable configuration and server configuration.
    """
    # The starting execution point of the app.
    FASTAPI_APP = 'main.py'


class DevelopmentConfig(BaseAppConfig):
    """
        This class for generates the config for development instance.
    """
    DEBUG: bool = True
    TESTING: bool = False
    SQLALCHEMY_DATABASE_URL = Settings().SQLALCHEMY_DATABASE_URL
