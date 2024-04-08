from flask import Blueprint, jsonify, request

from app.models import User, db

user_blueprint = Blueprint('users', __name__, url_prefix="/users")


@user_blueprint.route("/get_all", methods=["GET"])
def get_users():
    users = User.query.all()
    users_list = []
    for user in users:
        users_list.append(user.to_dict())

    return jsonify(users_list), 200;


@user_blueprint.route("/get_by_id/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"message": "User not found"}), 404
    else:
        return jsonify(user.to_dict()), 200


@user_blueprint.route("/create", methods=["POST"])
def create_user():
    data = request.get_json()
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201


@user_blueprint.route("/update/<int:id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"message": "User not found"}), 404
    else:
        for key, value in data.items():
            setattr(user, key, value)
        db.session.commit()
        return jsonify(user.to_dict()), 200


@user_blueprint.route("/get_by_username/<string:username>", methods=["GET"])
def get_user_by_username(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({"message": "User not found"}), 404
    else:
        return jsonify(user.to_dict()), 200
