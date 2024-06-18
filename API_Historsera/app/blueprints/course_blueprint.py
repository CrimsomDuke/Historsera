from datetime import datetime

from flask import Blueprint, jsonify, request

from app.models import Course, db

course_blueprint = Blueprint('courses', __name__, url_prefix="/courses")

@course_blueprint.route("/get_all", methods=["GET"])
def get_all_courses():
    courses = Course.query.all()
    courses_list = []
    for course in courses:
        courses_list.append(course.to_dict())
    return jsonify(courses_list), 200;

@course_blueprint.route("/get_by_id/<int:course_id>", methods=["GET"])
def get_course(course_id):
    course = Course.query.get(course_id)
    if course is None:
        return jsonify({"message": "Course not found"}), 404
    else:
        return jsonify(course.to_dict()), 200

@course_blueprint.route("/create", methods=["POST"])
def create_course():
    data = request.get_json()
    course = Course(**data)
    db.session.add(course)
    db.session.commit()
    return jsonify(course.to_dict()), 201

@course_blueprint.route("/update/<int:course_id>", methods=["PUT"])
def update_course(course_id):
    data = request.get_json()
    course = Course.query.get(course_id)
    if course is None:
        return jsonify({"message": "Course not found"}), 404
    else:
        for key, value in data.items():
            setattr(course, key, value)
        db.session.commit()
        return jsonify(course.to_dict()), 200

@course_blueprint.route("/delete/<int:course_id>", methods=["DELETE"])
def delete_course(course_id):
    course = Course.query.get(course_id)
    if course is None:
        return jsonify({"message": "Course not found"}), 404
    else:
        db.session.delete(course)
        db.session.commit()
        return jsonify({"message": "Course deleted"}), 200

@course_blueprint.route("/get_by_category/<string:category_name>", methods=["GET"])
def get_courses_by_category(category_name):
    print(Course.category_name.like(f"%{category_name}%"));
    courses = Course.query.filter(Course.category_name.like(f"%{category_name}%")).all()
    courses_list = []
    for course in courses:
        courses_list.append(course.to_dict())
    return jsonify(courses_list), 200

@course_blueprint.route("/get_by_author/<string:author>", methods=["GET"])
def get_courses_by_author(author):
    courses = Course.query.filter(Course.author.like(f"%{author}%")).all()
    courses_list = []
    for course in courses:
        courses_list.append(course.to_dict())
    return jsonify(courses_list), 200

@course_blueprint.route("/get_by_name/<string:course_name>", methods=["GET"])
def get_courses_by_name(course_name):
    courses = Course.query.filter(Course.course_name.like(f"%{course_name}%")).all()
    courses_list = []
    for course in courses:
        courses_list.append(course.to_dict())
    return jsonify(courses_list), 200

#search courses by name, author and category
@course_blueprint.route("/search", methods=["POST"])
def search_courses():
    data = request.get_json()
    search_val = data.get('search')
    print(search_val);
    courses = None;
    if(search_val is None or search_val == "" or search_val == "1 = 1"):
        #get all courses
        courses = Course.query.all()
    else:
        courses = Course.query.filter(Course.course_name.like(f"%{search_val}%") | Course.author.like(f"%{search_val}%") | Course.category_name.like(f"%{search_val}%")).all()

    courses_list = []
    for course in courses:
        courses_list.append(course.to_dict())
    return jsonify(courses_list), 200