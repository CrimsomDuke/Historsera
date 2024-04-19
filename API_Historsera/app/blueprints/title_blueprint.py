from flask import Blueprint, jsonify, request
from app.models import Title, db

title_blueprint = Blueprint('titles', __name__, url_prefix="/titles")

@title_blueprint.route("/get_all", methods=["GET"])
def get_all_titles():
    titles = Title.query.all()
    titles_list = []
    for title in titles:
        titles_list.append(title.to_dict())
    return jsonify(titles_list), 200;

@title_blueprint.route("/get_by_title_name/<string:title_name>", methods=["GET"])
def get_title(title_name):
    title = Title.query.filter(Title.title_name == title_name).first()
    if title is None:
        return jsonify({"message": "Title not found"}), 404
    else:
        return jsonify(title.to_dict()), 200

@title_blueprint.route("/create", methods=["POST"])
def create_title():
    data = request.get_json()
    title = Title(**data)
    db.session.add(title)
    db.session.commit()
    return jsonify(title.to_dict()), 201

@title_blueprint.route("/delete/<string:title_name>", methods=["DELETE"])
def delete_title(title_name):
    title = Title.query.filter(Title.title_name == title_name).first()
    if title is None:
        return jsonify({"message": "Title not found"}), 404
    else:
        db.session.delete(title)
        db.session.commit()
        return jsonify({"message": "Title deleted"}), 200