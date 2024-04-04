import jinja_partials
from flask import Flask

from app.blueprints import home_bp
from app.config import get_config_object
from app.extensions import toolbar


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(get_config_object())

    register_extensions(app)
    register_blueprints(app)

    return app


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(home_bp)


def register_extensions(app: Flask) -> None:
    jinja_partials.register_extensions(app)
    toolbar.init_app(app)
