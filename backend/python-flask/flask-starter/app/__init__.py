from flask import Flask
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)

    from .routes.root import root as root_blueprint
    app.register_blueprint(root_blueprint)

    from .routes.health import health as health_blueprint
    app.register_blueprint(health_blueprint)

    return app
