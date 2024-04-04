import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    FLASK_ENV: str
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "default_development_secret_key")


class DevelopmentConfig(Config):
    FLASK_ENV = "development"

    # Debug toolbar configurations.
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEBUG_TB_PROFILER_ENABLED = True
    DEBUG_TB_TEMPLATE_EDITOR_ENABLED = True


class TestingConfig(Config):
    FLASK_ENV = "testing"
    TESTING = True


def get_config_object() -> type[Config]:
    app_env = os.environ.get("ENV", "development")
    config_mapping: dict[str, type[Config]] = {
        cls.FLASK_ENV: cls for cls in Config.__subclasses__()
    }

    if app_env not in config_mapping:
        msg = "Invalid environment set in .env file."
        raise RuntimeError(msg)

    return config_mapping[app_env]
