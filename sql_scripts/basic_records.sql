
-- BASIC INSERTS ON THE TABLES

-- INSERT ADMIN USER
INSERT INTO tbl_users(username, email, user_password)
VALUES('admin', 'admin@gmail.com', 'admin!123');

INSERT INTO tbl_administrators values(1);

--INSERT NORMAL USERS
INSERT INTO tbl_users(username, email, user_password)
VALUES ('sewojtek', 'sebas@gmail.com', 'password1');

--INSERT CATEGORIES
INSERT INTO tbl_categories VALUES ('Historia antigua');

-- INSERT COURSES
INSERT INTO tbl_courses (course_name, author, description, ref_image_path, category_name)
VALUES ('Historia de la antigua Grecia', 'Ryan Stitt', 'Este curso explorará la historia de la Grecia antigua y sus aportes',
'C:\Users\PC\Desktop\CrimsomDuke\tareas\Semestre_5\Web_I\Final_Project\Historsera\media\images', 'Historia antigua');

INSERT INTO tbl_courses (course_name, author, description, ref_image_path, category_name)
VALUES ('TESTING ORDER', 'Ryan TEST', 'Este curso explorará TESTS',
'C:\Users\PC\Desktop\CrimsomDuke\tareas\Semestre_5\Web_I\Final_Project\Historsera\media\images', 'Historia antigua');

--INSERT LECTURES
INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Que sea Grecia!', 'Veamos como inicia grecia', TRUE, NULL, 
'https://www.youtube.com/watch?v=AlHn5bi-KiY&list=PLYoEIAhIdxYsn0Hael8PfYTbirBrvo6QR&index=1&pp=iAQB', 1);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('TEST LECT', 'AVANZANDO cON TEST', TRUE, NULL, 
'https://www.youtube.com/watch?v=AlHn5bi-KiY&list=PLYoEIAhIdxYsn0Hael8PfYTbirBrvo6QR&index=1&pp=iAQB', 2);

-- INSERT RELATIONSHIPS
INSERT INTO tbl_user_enrolled_in_course VALUES (1, 1);
INSERT INTO tbl_user_takes_lecture VALUES (1, 1);

-- first titles in the db
INSERT INTO tbl_titles (title_name) VALUES ('The Rookie');
INSERT INTO tbl_titles (title_name) VALUES ('Rata de plataforma');
INSERT INTO tbl_titles (title_name) VALUES ('Historiador atolondrado');
INSERT INTO tbl_titles (title_name) VALUES ('Discipulo de Suetonio');
INSERT INTO tbl_titles (title_name) VALUES ('Memoria Aurea');
INSERT INTO tbl_titles (title_name) VALUES ('Maestro Neo-erudito');

-- SHOW RESULTS
SELECT * FROM tbl_users tu;
SELECT * FROM tbl_administrators ta;
SELECT * FROM tbl_categories tc;
SELECT * FROM tbl_courses tc;
SELECT * FROM tbl_lectures tl ORDER BY course_id, order_num;
SELECT * FROM tbl_user_enrolled_in_course tueic;
SELECT * FROM tbl_user_takes_lecture tutl;
