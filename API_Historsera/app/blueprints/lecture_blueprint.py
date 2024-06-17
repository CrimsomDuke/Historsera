from flask import Blueprint, jsonify, request
from app.models import Lecture, db

lecture_blueprint = Blueprint('lectures', __name__, url_prefix="/lectures")

@lecture_blueprint.route("/get_all", methods=["GET"])
def get_all_lectures():
    lectures = Lecture.query.all()
    lectures_list = []
    for lecture in lectures:
        lectures_list.append(lecture.to_dict())
    return jsonify(lectures_list), 200;

@lecture_blueprint.route("/get_by_id/<int:lecture_id>", methods=["GET"])
def get_lecture(lecture_id):
    lecture = Lecture.query.get(lecture_id)
    if lecture is None:
        return jsonify({"message": "Lecture not found"}), 404
    return jsonify(lecture.to_dict()), 200;

@lecture_blueprint.route("/get_by_course_id/<int:course_id>", methods=["GET"])
def get_lectures_by_course_id(course_id):
    #order by order_num
    lectures = Lecture.query.filter_by(course_id=course_id).order_by(Lecture.order_num).all()
    lectures_list = []
    for lecture in lectures:
        lectures_list.append(lecture.to_dict())
    return jsonify(lectures_list), 200;

@lecture_blueprint.route("/create", methods=["POST"])
def create_lecture():
    data = request.get_json()
    lecture = Lecture(**data)
    db.session.add(lecture)
    db.session.commit()
    return jsonify(lecture.to_dict()), 201

@lecture_blueprint.route("/delete/<int:lecture_id>", methods=["DELETE"])
def delete_lecture(lecture_id):
    lecture = Lecture.query.get(lecture_id)
    if lecture is None:
        return jsonify({"message": "Lecture not found"}), 404
    else:
        db.session.delete(lecture)
        db.session.commit()
        return jsonify({"message": "Lecture deleted"}), 200

@lecture_blueprint.route("/update/<int:lecture_id>", methods=["PUT"])
def update_lecture(lecture_id):
    data = request.get_json()
    lecture = Lecture.query.get(lecture_id)
    if lecture is None:
        return jsonify({"message": "Lecture not found"}), 404
    else:
        for key, value in data.items():
            setattr(lecture, key, value)
        db.session.commit()
        return jsonify(lecture.to_dict()), 200

@lecture_blueprint.route("/change_order/<int:lecture_id>/<int:new_order>", methods=["PUT"])
def change_order(lecture_id, new_order):
    lecture = Lecture.query.get(lecture_id)
    if lecture is None:
        return jsonify({"message": "Lecture not found"}), 404
    else:
        lecture.order_num = new_order
        db.session.commit()
        return jsonify(lecture.to_dict()), 200