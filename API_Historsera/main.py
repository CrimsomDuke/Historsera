from flask import Flask, jsonify
from flask_cors import CORS
from app.config import DevelopmentConfig
from app import create_app
from app.models import db

app = create_app()
db.init_app(app);
CORS(app);


@app.route('/')
def index():
    endpoints = {
        'users': '/users',
        'courses': '/courses',
        'categories': '/categories',
        'lectures': '/lectures',
        'administrators': '/administrators',
        'titles': '/titles',
        'user_takes_lecture': '/user_takes_lecture',
        'user_enrolled_in_course': '/user_enrolled_in_course',
    }

    return jsonify(endpoints)


if __name__ == '__main__':
    app.run(debug=True)
