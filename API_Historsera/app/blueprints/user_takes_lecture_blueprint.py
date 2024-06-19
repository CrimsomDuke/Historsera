from flask import Blueprint, jsonify, request
from app.models import UserTakesLecture, User, Lecture, Course, db

user_takes_lecture_blueprint = Blueprint('user_takes_lecture', __name__, url_prefix="/user_takes_lecture")

@user_takes_lecture_blueprint.route("/get_all", methods=["GET"])
def get_all_user_takes_lectures():
    user_takes_lectures = UserTakesLecture.query.all()
    user_takes_lectures_list = []
    users = []
    lectures = []
    for user_takes_lecture in user_takes_lectures:
        user = User.query.get(user_takes_lecture.user_id)
        lecture = Lecture.query.get(user_takes_lecture.lecture_id)
        users.append(user)
        lectures.append(lecture)

    for user, lecture in zip(users, lectures):
        user_takes_lectures_list.append({"user": user.to_dict(), "lecture": lecture.to_dict()})

    return jsonify(user_takes_lectures_list), 200;

@user_takes_lecture_blueprint.route("/get_by_user_id/<int:user_id>", methods=["GET"])
def get_user_takes_lecture(user_id):
    user_takes_lectures = UserTakesLecture.query.filter_by(user_id=user_id).all()
    user_takes_lectures_list = []
    lectures = []
    #get the lectures objects
    for user_takes_lecture in user_takes_lectures:
        lecture = Lecture.query.get(user_takes_lecture.lecture_id)
        lectures.append(lecture)

    for lecture in lectures:
        user_takes_lectures_list.append(lecture.to_dict())

    return jsonify(user_takes_lectures_list), 200

@user_takes_lecture_blueprint.route("/get_by_lecture_id/<int:lecture_id>", methods=["GET"])
def get_user_takes_lecture_by_lecture_id(lecture_id):
    user_takes_lectures = UserTakesLecture.query.filter_by(lecture_id=lecture_id).all()
    user_takes_lectures_list = []
    users = []
    for user_takes_lecture in user_takes_lectures:
        user = User.query.get(user_takes_lecture.user_id)
        users.append(user)

    for user in users:
        user_takes_lectures_list.append(user.to_dict())
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

@user_takes_lecture_blueprint.route("/get_by_user_id_and_course_id/", methods=["GET"])
def get_user_takes_lecture_by_user_id_and_course_id():
    #params of the search
    user_id = request.args.get('user_id')
    course_id = request.args.get('course_id')

    #given the params of user and course, get the lectures in which the user is enrolled
    # and the course is the same as the lectures course

    user_takes_lectures = UserTakesLecture.query.join(Lecture, UserTakesLecture.lecture_id == Lecture.lecture_id).filter(UserTakesLecture.user_id == user_id, Lecture.course_id == course_id).all()
    user_takes_lectures_list = []
    lectures = []
    #get the lectures objects
    for user_takes_lecture in user_takes_lectures:
        lecture = Lecture.query.get(user_takes_lecture.lecture_id)
        lectures.append(lecture)

    for lecture in lectures:
        user_takes_lectures_list.append(lecture.to_dict())

    return jsonify(user_takes_lectures_list), 200

@user_takes_lecture_blueprint.route("/create", methods=["POST"])
def create_user_takes_lecture():
    data = request.get_json()
    user_takes_lecture = UserTakesLecture()

    user_takes_lecture.user_id = data['user_id']
    user_takes_lecture.lecture_id = data['lecture_id']
    user_takes_lecture.is_finished = False

    #check if the user is already enrolled in the lecture
    user_takes_lecture_check = UserTakesLecture.query.filter_by(user_id=user_takes_lecture.user_id, lecture_id=user_takes_lecture.lecture_id).first()
    if user_takes_lecture_check is not None:
        return jsonify({"message": "User already takes this lecture"}), 400
    #if not, then we talke the lecture
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



#check is the user has completed the lecture
@user_takes_lecture_blueprint.route("/check_finished", methods=["GET"])
def check_finished():
    #params of the search
    user_id = request.args.get('user_id')
    lecture_id = request.args.get('lecture_id')

    user_takes_lecture = UserTakesLecture.query.filter_by(user_id=user_id, lecture_id=lecture_id).first()
    if user_takes_lecture is None:
        return jsonify({"message": "User takes lecture not found"}), 404
    else:
        return jsonify({"completed": user_takes_lecture.is_finished}), 200


@user_takes_lecture_blueprint.route("/complete_lecture", methods=["PUT"])
def complete_lecture():
    #params of json
    data = request.get_json()
    user_id = data['user_id']
    lecture_id = data['lecture_id']

    user_takes_lecture = UserTakesLecture.query.filter_by(user_id=user_id, lecture_id=lecture_id).first()
    if user_takes_lecture is None:
        return jsonify({"message": "User takes lecture not found"}), 404
    else:
        user_takes_lecture.is_finished = True
        db.session.commit()
        return jsonify(user_takes_lecture.to_dict()), 200
