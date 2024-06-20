from flask import Blueprint, jsonify, request
from app.models import Administrator, User, db

administrator_blueprint = Blueprint('administrators', __name__, url_prefix="/administrators")


@administrator_blueprint.route("/get_all", methods=["GET"])
def get_all_administrators():
    administrators = Administrator.query.all()
    administrators_list = []
    for administrator in administrators:
        administrators_list.append(administrator.to_dict())
    return jsonify(administrators_list), 200;


@administrator_blueprint.route("/get_by_id/<int:administrator_id>", methods=["GET"])
def get_administrator(administrator_id):
    administrator = Administrator.query.get(administrator_id)
    if administrator is None:
        return jsonify({"message": "Administrator not found"}), 404
    else:
        return jsonify(administrator.to_dict()), 200


@administrator_blueprint.route("/get_admin_by_user_id/<int:administrator_id>", methods=["GET"])
def get_admin_user(administrator_id):
    administrator = Administrator.query.get(administrator_id)
    user = User.query.get(administrator_id)
    if administrator is not None and user is not None:
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({"message": "Administrator not found"}), 404

@administrator_blueprint.route("/create", methods=["POST"])
def create_administrator():
    data = request.get_json()
    administrator = Administrator(**data)
    db.session.add(administrator)
    db.session.commit()
    return jsonify(administrator.to_dict()), 201

@administrator_blueprint.route("/delete/<int:administrator_id>", methods=["DELETE"])
def delete_administrator(administrator_id):
    administrator = Administrator.query.get(administrator_id)
    if administrator is None:
        return jsonify({"message": "Administrator not found"}), 404
    else:
        db.session.delete(administrator)
        db.session.commit()
        return jsonify({"message": "Administrator deleted"}), 200
