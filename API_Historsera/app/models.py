from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy();


# models

class User(db.Model):
    __tablename__ = 'tbl_users';
    id = db.Column(db.Integer, primary_key=True);
    username = db.Column(db.String(20));
    email = db.Column(db.String(70));
    user_password = db.Column(db.String(12));
    creation_date = db.Column(db.Date);
    points = db.Column(db.Integer);
    title_name = db.Column(db.String(100));

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "user_password": self.user_password,
            "creation_date": self.creation_date,
            "points": self.points,
            "title_name": self.title_name
        }


class Course(db.Model):
    __tablename__ = 'tbl_courses';
    course_id = db.Column(db.Integer, primary_key=True);
    course_name = db.Column(db.String(100));
    author = db.Column(db.String(50));
    description = db.Column(db.String(350));
    ref_image_path = db.Column(db.String(350));
    category_name = db.Column(db.String(150));

    def to_dict(self):
        return {
            "course_id": self.course_id,
            "course_name": self.course_name,
            "author": self.author,
            "description": self.description,
            "ref_image_path": self.ref_image_path,
            "category_name": self.category_name
        }


class Category(db.Model):
    __tablename__ = 'tbl_categories';
    category_name = db.Column(db.String(150), primary_key=True);

    def to_dict(self):
        return {
            "category_name": self.category_name
        }


class Lecture(db.Model):
    __tablename__ = 'tbl_lectures';
    lecture_id = db.Column(db.Integer, primary_key=True);
    title = db.Column(db.String(100));
    description = db.Column(db.String(350));
    is_video = db.Column(db.Boolean);
    file_path = db.Column(db.String(350));
    link = db.Column(db.String(350));
    duration_sec = db.Column(db.Integer);
    course_id = db.Column(db.Integer, db.ForeignKey('tbl_courses.course_id'));

    def to_dict(self):
        return {
            "lecture_id": self.lecture_id,
            "title": self.title,
            "description": self.description,
            "is_video": self.is_video,
            "file_path": self.file_path,
            "link": self.link,
            "duration_sec": self.duration_sec,
            "course_id": self.course_id
        }

class Administrator(db.Model):
    __tablename__ = 'tbl_administrators';
    user_id = db.Column(db.Integer, db.ForeignKey('tbl_users.id'), primary_key=True);

    def to_dict(self):
        return {
            "user_id": self.user_id
        }


class Title(db.Model):
    __tablename__ = 'tbl_titles';
    title_name = db.Column(db.String(100), primary_key=True);

    def to_dict(self):
        return {
            "title_name": self.title_name
        }


class UserTakesLecture(db.Model):
    __tablename__ = 'tbl_user_takes_lecture';
    user_id = db.Column(db.Integer, db.ForeignKey('tbl_users.id'), primary_key=True);
    lecture_id = db.Column(db.Integer, db.ForeignKey('tbl_lectures.lecture_id'), primary_key=True);
    is_finished = db.Column(db.Boolean);

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "lecture_id": self.lecture_id,
            "is_finished": self.is_finished
        }


class UserEnrolledInCourse(db.Model):
    __tablename__ = 'tbl_user_enrolled_in_course';
    user_id = db.Column(db.Integer, db.ForeignKey('tbl_users.id'), primary_key=True);
    course_id = db.Column(db.Integer, db.ForeignKey('tbl_courses.course_id'), primary_key=True);
    is_finished = db.Column(db.Boolean);

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "course_id": self.course_id,
            "is_finished": self.is_finished
        }
