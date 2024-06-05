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
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        #get the extension of the file and create a new filename, the extension is the last 4 characters of the filenameç
        components = file.filename.split('.')

        extension = components[len(components) - 1];

        if(extension in ['jpg', 'jpeg', 'png']):
            #get the daate in format yyyy-mm-dd-hh-mm-ss
            filename = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.' + extension;

            file.save(os.path.join(app.config['IMAGES_FOLDER'], filename))
            return jsonify({'success': 'File successfully uploaded'}), 200
        if(extension == 'pdf'):
            filename = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.' + extension;
            file.save(os.path.join(app.config['PDFS_FOLDER'], filename))
            return jsonify({'success': 'File successfully uploaded'}), 200

        else:
            return jsonify({'error': 'Invalid file extension'}), 400

if __name__ == '__main__':
    app.run(debug=True)
