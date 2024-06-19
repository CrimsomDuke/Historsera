from flask import Blueprint, jsonify, request
from app.models import UserEnrolledInCourse, User, Course, db

user_enrolled_in_course_blueprint = Blueprint('user_enrolled_in_course', __name__, url_prefix="/user_enrolled_in_course")

@user_enrolled_in_course_blueprint.route("/get_all", methods=["GET"])
def get_all_user_enrolled_in_courses():
    user_enrolled_in_courses = UserEnrolledInCourse.query.all()
    users = []
    courses = []
    for user_enrolled_in_course in user_enrolled_in_courses:
        user = User.query.get(user_enrolled_in_course.user_id)
        course = Course.query.get(user_enrolled_in_course.course_id)
        users.append(user)
        courses.append(course)

    user_enrolled_in_courses_list = []
    for user, course in zip(users, courses):
        user_enrolled_in_courses_list.append({"user": user.to_dict(), "course": course.to_dict()})
    return jsonify(user_enrolled_in_courses_list), 200;

@user_enrolled_in_course_blueprint.route("/get_by_user_id/<int:user_id>", methods=["GET"])
def get_user_enrolled_in_course(user_id):
    user_enrolled_in_courses = UserEnrolledInCourse.query.filter_by(user_id=user_id).all()
    user_enrolled_in_courses_list = []

    courses = []
    #get the courses objects
    for user_enrolled_in_course in user_enrolled_in_courses:
        course = Course.query.get(user_enrolled_in_course.course_id)
        courses.append(course)

    for course in courses:
        user_enrolled_in_courses_list.append(course.to_dict())

    return jsonify(user_enrolled_in_courses_list), 200

@user_enrolled_in_course_blueprint.route("/get_by_course_id/<int:course_id>", methods=["GET"])
def get_user_enrolled_in_course_by_course_id(course_id):
    user_enrolled_in_courses = UserEnrolledInCourse.query.filter_by(course_id=course_id).all()
    users = []
    for user_enrolled_in_course in user_enrolled_in_courses:
        user = User.query.get(user_enrolled_in_course.user_id)
        course = Course.query.get(user_enrolled_in_course.course_id)
        users.append(user)

    user_enrolled_in_courses_list = []
    for user in users:
        user_enrolled_in_courses_list.append(user.to_dict())
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

