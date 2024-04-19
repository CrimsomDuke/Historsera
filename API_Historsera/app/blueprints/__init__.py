
from flask.blueprints import Blueprint;
from .user_blueprint import user_blueprint;
from .course_blueprint import course_blueprint;
from .category_blueprint import category_blueprint;
from .lecture_blueprint import lecture_blueprint;
from .administrator_blueprint import administrator_blueprint;
from .user_takes_lecture_blueprint import user_takes_lecture_blueprint;
from .user_enrolled_in_course_blueprint import user_enrolled_in_course_blueprint;