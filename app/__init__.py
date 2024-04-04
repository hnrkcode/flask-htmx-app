import jinja_partials
from flask import Flask

from app.blueprints import home_bp
from app.config import CONFIG_OBJECT
from app.extensions import toolbar


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(CONFIG_OBJECT)

    register_extensions(app)
    register_blueprints(app)

    return app


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(home_bp)


def register_extensions(app: Flask) -> None:
    jinja_partials.register_extensions(app)
    toolbar.init_app(app)
