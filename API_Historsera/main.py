import os

from flask import Flask, jsonify, request
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
    print(app.config['IMAGES_FOLDER']);
    return jsonify(endpoints)



@app.route('/upload_file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        filename = file.filename
        file.save(os.path.join(app.config['IMAGES_FOLDER'], filename))
        return jsonify({'success': 'File successfully uploaded'}), 200

if __name__ == '__main__':
    app.run(debug=True)
