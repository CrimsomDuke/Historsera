from flask import Flask
from app.config import DevelopmentConfig

from app.blueprints import user_blueprint, course_blueprint, category_blueprint, lecture_blueprint, administrator_blueprint, user_takes_lecture_blueprint, user_enrolled_in_course_blueprint

def create_app():
    app = Flask(__name__);
    app.config.from_object(DevelopmentConfig);

    app.register_blueprint(user_blueprint);
    app.register_blueprint(course_blueprint);
    app.register_blueprint(category_blueprint);
    app.register_blueprint(lecture_blueprint);
    app.register_blueprint(administrator_blueprint);
    app.register_blueprint(user_takes_lecture_blueprint);
    app.register_blueprint(user_enrolled_in_course_blueprint);

    return app;