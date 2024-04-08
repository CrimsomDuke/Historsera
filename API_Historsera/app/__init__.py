from flask import Flask
from app.config import DevelopmentConfig

from app.blueprints import user_blueprint

def create_app():
    app = Flask(__name__);
    app.config.from_object(DevelopmentConfig);

    app.register_blueprint(user_blueprint);

    return app;