from flask import Blueprint, jsonify, request
from app.models import UserEnrolledInCourse, db

user_enrolled_in_course_blueprint = Blueprint('user_enrolled_in_course', __name__, url_prefix="/user_enrolled_in_course")

@user_enrolled_in_course_blueprint.route("/get_all", methods=["GET"])
def get_all_user_enrolled_in_courses():
    user_enrolled_in_courses = UserEnrolledInCourse.query.all()
    user_enrolled_in_courses_list = []
    for user_enrolled_in_course in user_enrolled_in_courses:
        user_enrolled_in_courses_list.append(user_enrolled_in_course.to_dict())
    return jsonify(user_enrolled_in_courses_list), 200;

@user_enrolled_in_course_blueprint.route("/get_by_user_id/<int:user_id>", methods=["GET"])
def get_user_enrolled_in_course(user_id):
    user_enrolled_in_courses = UserEnrolledInCourse.query.filter_by(user_id=user_id).all()
    user_enrolled_in_courses_list = []
    for user_enrolled_in_course in user_enrolled_in_courses:
        user_enrolled_in_courses_list.append(user_enrolled_in_course.to_dict())
    return jsonify(user_enrolled_in_courses_list), 200

@user_enrolled_in_course_blueprint.route("/get_by_course_id/<int:course_id>", methods=["GET"])
def get_user_enrolled_in_course_by_course_id(course_id):
    user_enrolled_in_courses = UserEnrolledInCourse.query.filter_by(course_id=course_id).all()
    user_enrolled_in_courses_list = []
    for user_enrolled_in_course in user_enrolled_in_courses:
        user_enrolled_in_courses_list.append(user_enrolled_in_course.to_dict())
    return jsonify(user_enrolled_in_courses_list), 200

@user_enrolled_in_course_blueprint.route("/get_by_user_course", methods=["GET"])
def get_user_enrolled_in_course_by_user_course():
    #params of the search
    user_id = request.args.get('user')
    course_id = request.args.get('course')

    user_enrolled_in_course = UserEnrolledInCourse.query.filter_by(user_id=user_id, course_id=course_id).first()
    if user_enrolled_in_course is None:
        return jsonify({"message": "User enrolled in course not found"}), 404
    else:
        return jsonify(user_enrolled_in_course.to_dict()), 200

@user_enrolled_in_course_blueprint.route("/create", methods=["POST"])
def create_user_enrolled_in_course():
    data = request.get_json()
    user_enrolled_in_course = UserEnrolledInCourse(**data)
    db.session.add(user_enrolled_in_course)
    db.session.commit()
    return jsonify(user_enrolled_in_course.to_dict()), 201

@user_enrolled_in_course_blueprint.route("/delete", methods=["DELETE"])
def delete_user_enrolled_in_course():
    #params of the search
    user_id = request.args.get('user')
    course_id = request.args.get('course')

    user_enrolled_in_course = UserEnrolledInCourse.query.filter_by(user_id=user_id, course_id=course_id).first()
    if user_enrolled_in_course is None:
        return jsonify({"message": "User enrolled in course not found"}), 404
    else:
        db.session.delete(user_enrolled_in_course)
        db.session.commit()
        return jsonify({"message" : "user_enrolled_in_course deleted"}), 200

