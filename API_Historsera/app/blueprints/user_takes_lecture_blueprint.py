from flask import Blueprint, jsonify, request
from app.models import UserTakesLecture, db

user_takes_lecture_blueprint = Blueprint('user_takes_lecture', __name__, url_prefix="/user_takes_lecture")

@user_takes_lecture_blueprint.route("/get_all", methods=["GET"])
def get_all_user_takes_lectures():
    user_takes_lectures = UserTakesLecture.query.all()
    user_takes_lectures_list = []
    for user_takes_lecture in user_takes_lectures:
        user_takes_lectures_list.append(user_takes_lecture.to_dict())
    return jsonify(user_takes_lectures_list), 200;

@user_takes_lecture_blueprint.route("/get_by_user_id/<int:user_id>", methods=["GET"])
def get_user_takes_lecture(user_id):
    user_takes_lectures = UserTakesLecture.query.filter_by(user_id=user_id).all()
    user_takes_lectures_list = []
    for user_takes_lecture in user_takes_lectures:
        user_takes_lectures_list.append(user_takes_lecture.to_dict())
    return jsonify(user_takes_lectures_list), 200

@user_takes_lecture_blueprint.route("/get_by_lecture_id/<int:lecture_id>", methods=["GET"])
def get_user_takes_lecture_by_lecture_id(lecture_id):
    user_takes_lectures = UserTakesLecture.query.filter_by(lecture_id=lecture_id).all()
    user_takes_lectures_list = []
    for user_takes_lecture in user_takes_lectures:
        user_takes_lectures_list.append(user_takes_lecture.to_dict())
    return jsonify(user_takes_lectures_list), 200

@user_takes_lecture_blueprint.route("/get_by_user_lecture", methods=["GET"])
def get_user_takes_lecture_by_user_lecture():
    #params of the search
    user_id = request.args.get('user')
    lecture_id = request.args.get('lecture')

    user_takes_lecture = UserTakesLecture.query.filter_by(user_id=user_id, lecture_id=lecture_id).first()
    if user_takes_lecture is None:
        return jsonify({"message": "User takes lecture not found"}), 404
    else:
        return jsonify(user_takes_lecture.to_dict()), 200

@user_takes_lecture_blueprint.route("/create", methods=["POST"])
def create_user_takes_lecture():
    data = request.get_json()
    user_takes_lecture = UserTakesLecture(**data)
    db.session.add(user_takes_lecture)
    db.session.commit()
    return jsonify(user_takes_lecture.to_dict()), 201

@user_takes_lecture_blueprint.route("/delete", methods=["DELETE"])
def delete_user_takes_lecture():
    #params of the search
    user_id = request.args.get('user')
    lecture_id = request.args.get('lecture')

    user_takes_lecture = UserTakesLecture.query.filter_by(user_id=user_id, lecture_id=lecture_id).first()
    if user_takes_lecture is None:
        return jsonify({"message": "User takes lecture not found"}), 404
    else:
        db.session.delete(user_takes_lecture)
        db.session.commit()
        return jsonify({"message": "User takes lecture deleted"}), 200
