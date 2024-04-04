import os

from dotenv import load_dotenv

load_dotenv()


class Config:
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


app_env = os.environ.get("ENV", "development")

config_mapping = {
    "development": "app.config.DevelopmentConfig",
    "testing": "app.config.TestingConfig",
}

CONFIG_OBJECT = config_mapping.get(app_env)

if CONFIG_OBJECT is None:
    msg = "Invalid environment set in .env file."
    raise RuntimeError(msg)
