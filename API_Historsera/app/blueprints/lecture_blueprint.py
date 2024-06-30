from flask import Blueprint, jsonify, request
from sqlalchemy import text
from app.models import Lecture, UserTakesLecture, db

lecture_blueprint = Blueprint('lectures', __name__, url_prefix="/lectures")


@lecture_blueprint.route("/get_all", methods=["GET"])
def get_all_lectures():
    lectures = Lecture.query.order_by(Lecture.order_num).all()
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
    # order by order_num
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
    try:
        lecture = Lecture.query.get(lecture_id)

        #borrar las relaciones de la tabla UserTakesLecture
        user_takes_lectures = UserTakesLecture.query.filter_by(lecture_id=lecture_id).all()
        for user_takes_lecture in user_takes_lectures:
            db.session.delete(user_takes_lecture)
            db.session.commit()

        if lecture is None:
            return jsonify({"message": "Lecture not found"}), 404
        else:
            db.session.delete(lecture)
            db.session.commit()
            return jsonify({"message": "Lecture deleted"}), 200
    except Exception as e:
        return jsonify({"message": "Lecture has dependencies"}), 400


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


@lecture_blueprint.route("get_next_lecture_id", methods=["GET"])
def get_next_lecture_id():
    # params of the search
    lecture_id = request.args.get('lecture_id')

    lecture = Lecture.query.filter_by(lecture_id=lecture_id).first()

    lectures_in_course = Lecture.query.filter_by(course_id=lecture.course_id).order_by(Lecture.order_num).all()

    next_lecture_id = -1;
    if (lecture.order_num < len(lectures_in_course)):
        # obtenemos el id de la lectura siguiente en el orden del curso
        # de lo contrario, devolvemos -1
        next_lecture_id = lectures_in_course[lecture.order_num].lecture_id

    return jsonify({"next_lecture_id": next_lecture_id}), 200;


# get previous lecture
@lecture_blueprint.route("get_previous_lecture_id", methods=["GET"])
def get_previous_lecture_id():
    # params of the search
    lecture_id = request.args.get('lecture_id')

    lecture = Lecture.query.filter_by(lecture_id=lecture_id).first()

    lectures_in_course = Lecture.query.filter_by(course_id=lecture.course_id).order_by(Lecture.order_num).all()
    for l in lectures_in_course:
        print(l.to_dict())

    previous_lecture_id = -1;
    if (lecture.order_num > 1):
        # obtenemos el id de la lectura anterior en el orden del curso
        # de lo contrario, devolvemos -1
        previous_lecture_id = lectures_in_course[lecture.order_num - 2].lecture_id

    return jsonify({"previous_lecture_id": previous_lecture_id}), 200;


@lecture_blueprint.route("/change_order/<int:lecture_id>/<int:new_order>", methods=["PUT"])
def change_order(lecture_id, new_order):
    lecture = Lecture.query.get(lecture_id)
    if lecture is None:
        return jsonify({"message": "Lecture not found"}), 404
    else:
        #execute a SP
        sql = text("CALL sp_lec_change_order_num(:lecture_id, :new_order)")

        # Execute the SQL statement
        db.session.execute(sql, {"lecture_id": lecture_id, "new_order": new_order})

        # Commit the transaction
        db.session.commit()
        return jsonify({'new_order_num': lecture.order_num}), 200
