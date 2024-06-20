
from flask import Blueprint, jsonify, request
from app.models import Category, Course, db

category_blueprint = Blueprint('categories', __name__, url_prefix="/categories")

@category_blueprint.route("/get_all", methods=["GET"])
def get_all_categories():
    categories = Category.query.all()
    categories_list = []
    for category in categories:
        categories_list.append(category.to_dict())
    return jsonify(categories_list), 200;

@category_blueprint.route("/get_by_name/<string:category_name>", methods=["GET"])
def get_category(category_name):
    courses = Category.query.filter(Category.category_name.like(f"%{category_name}%")).all()
    courses_list = []
    for course in courses:
        courses_list.append(course.to_dict())
    return jsonify(courses_list), 200;

@category_blueprint.route("/create", methods=["POST"])
def create_category():
    data = request.get_json()
    category = Category(**data)
    db.session.add(category)
    db.session.commit()
    return jsonify(category.to_dict()), 201

@category_blueprint.route("/delete/<string:category_name>", methods=["DELETE"])
def delete_category(category_name):
    category = Category.query.get(category_name)

    #check if category is used
    courses = Course.query.filter_by(category_name=category_name).all()
    if len(courses) > 0:
        return jsonify({"message": "Category is used by courses"}), 400

    if category is None:
        return jsonify({"message": "Category not found"}), 404
    else:
        db.session.delete(category)
        db.session.commit()
        return jsonify({"message": "Category deleted"}), 200
