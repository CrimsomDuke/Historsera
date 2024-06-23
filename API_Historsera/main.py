import os

from flask import jsonify, request
from flask_cors import CORS
from app import create_app
from app.models import db

import datetime

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
        print('No file part');
        return jsonify({'error': 'No file part'}), 206 # 206 for nothing to load

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        components = file.filename.split('.')
        extension = components[-1]

        #DEVOLVER EL PATH DEL ARCHIVO
        if extension in ['jpg', 'jpeg', 'png']:
            filename = file.filename + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.' + extension
            file_path = os.path.join(app.config['IMAGES_FOLDER'], filename)
            file.save(file_path)
            return jsonify({'success': 'File successfully uploaded', 'path': file_path}), 200
        elif extension == 'pdf':
            filename = file.filename + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.' + extension
            file_path = os.path.join(app.config['PDFS_FOLDER'], filename)
            file.save(file_path)
            return jsonify({'success': 'File successfully uploaded', 'path': file_path}), 200
        else:
            return jsonify({'error': 'Invalid file extension'}), 406
    else:
        return jsonify({'error': 'File upload failed'}), 500

if __name__ == '__main__':
    app.run(debug=True)
