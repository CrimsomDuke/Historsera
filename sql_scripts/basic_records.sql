
-- BASIC INSERTS ON THE TABLES

-- INSERT ADMIN USER
INSERT INTO tbl_users(username, email, user_password)
VALUES('admin', 'admin@gmail.com', 'admin!123');

INSERT INTO tbl_administrators values(1);

--INSERT NORMAL USERS
INSERT INTO tbl_users(username, email, user_password)
VALUES ('sewojtek', 'sebas@gmail.com', 'password1');

INSERT INTO tbl_users(username, email, user_password)
VALUES ('CrimsomDuke', 'sebastianrengelclaros@gmail.com', 'password');

-- first titles in the db
INSERT INTO tbl_titles (title_name, points_required) VALUES ('The Rookie', 100);
INSERT INTO tbl_titles (title_name, points_required) VALUES ('Rata de plataforma', 150);
INSERT INTO tbl_titles (title_name, points_required) VALUES ('Historiador atolondrado', 200);
INSERT INTO tbl_titles (title_name, points_required) VALUES ('Discipulo de Suetonio', 500);
INSERT INTO tbl_titles (title_name, points_required) VALUES ('Memoria Aurea', 1000);
INSERT INTO tbl_titles (title_name, points_required) VALUES ('Maestro Neo-erudito', 6969);

--INSERT CATEGORIES
INSERT INTO tbl_categories VALUES ('Historia antigua');
INSERT INTO tbl_categories VALUES ('Historia medieval');
INSERT INTO tbl_categories VALUES ('Historia de America');
INSERT INTO tbl_categories VALUES ('Historia de las lenguas');
INSERT INTO tbl_categories VALUES ('Cultura');

-- INSERT COURSES
INSERT INTO tbl_courses (course_name, author, description, ref_image_path, category_name)
VALUES ('Historia de la antigua Grecia', 'Ryan Stitt', 'Este curso explorará la historia de la Grecia antigua y sus aportes',
'C:\MediaTemp\images\antique_greece_course.jpg', 'Historia antigua');

INSERT INTO tbl_courses (course_name, author, description, ref_image_path, category_name)
VALUES ('Antigua Persia', 'History with Cy', 'history of the peoples known as the Medes and the Persians.', 
'C:\MediaTemp\images\antique_persia.jpg', 'Historia antigua');

INSERT INTO tbl_courses (course_name, author, description, ref_image_path, category_name)
VALUES ('Historia de Roma', 'Timaeus', 'here shall we go from here? Wonder where we will be a year from now?',
'C:\MediaTemp\images\rome.jpg', 'Historia antigua');

INSERT INTO tbl_courses (course_name, author, description, ref_image_path, category_name)
VALUES ('Venecia', 'Epic History', 'Descubramros la historia de Venecia',
'C:\MediaTemp\images\venice.jpg', 'Historia medieval');

INSERT INTO tbl_courses (course_name, author, description, ref_image_path, category_name)
VALUES ('Estados Unidos de America', 'CrashCourse', 'The Spanish were definitely not peaceful colonizers, but what colonizers are peaceful?',
'C:\MediaTemp\images\usa.jpg', 'Historia de America');

INSERT INTO tbl_courses (course_name, author, description, ref_image_path, category_name)
VALUES ('Bolivia en el siglo XX', 'Carlos D. Mesa Gisbert', 'Historia de los pueblos indígenas de Bolivia desde sus orígenes.',
'C:\MediaTemp\images\bolivia.jpg', 'Historia de America');

INSERT INTO tbl_courses (course_name, author, description, ref_image_path, category_name)
VALUES ('Historia de Mexico', 'The Ambling Bristolian', 'The Mexicaan History',
'C:\MediaTemp\images\mexico.jpg', 'Historia de America');

INSERT INTO tbl_courses (course_name, author, description, ref_image_path, category_name)
VALUES ('Historia de la lengua inglesa', 'Jeroen Timmermans', 'The complete history of the english language',
'C:\MediaTemp\images\english.jpg', 'Historia de las lenguas');

INSERT INTO tbl_courses (course_name, author, description, ref_image_path, category_name)
VALUES ('Historia de la programacion', 'David Jackson', 'How programming is a thing',
'C:\MediaTemp\images\programming.jpg', 'Cultura');

INSERT INTO tbl_courses (course_name, author, description, ref_image_path, category_name)
VALUES ('Filosofia a traves de la historia', 'Wheaton College', 'Como la filosofia se desarrolló',
'C:\MediaTemp\images\philosophy.jpg', 'Cultura');


--INSERT LECTURES

--curso 1
INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Que sea Grecia!', 'Veamos como inicia grecia', TRUE, 
'C:\MediaTemp\pdfs\sample-1.pdf',
'https://www.youtube.com/watch?v=AlHn5bi-KiY&list=PLYoEIAhIdxYsn0Hael8PfYTbirBrvo6QR&index=1&pp=iAQB', 1);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Genesis Griego', 'Inicios de la cultura', TRUE, NULL, 
'https://www.youtube.com/watch?v=pJFCKwQ4SeY&list=PLYoEIAhIdxYsn0Hael8PfYTbirBrvo6QR&index=2&pp=iAQB', 1);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('La edad de piedra', 'Primeros griegos', TRUE, NULL, 
'https://www.youtube.com/watch?v=RoL690rIxSA&list=PLYoEIAhIdxYsn0Hael8PfYTbirBrvo6QR&index=3&pp=iAQB', 1);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Inicios de la edad de Bronce', 'Edad de bronce griega', TRUE, NULL, 
'https://www.youtube.com/watch?v=5kR7_BGp4sQ&list=PLYoEIAhIdxYsn0Hael8PfYTbirBrvo6QR&index=4&pp=iAQB', 1);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Creta', 'Creta como base griega', TRUE, NULL, 
'https://www.youtube.com/watch?v=yMnxXKXG0ac&list=PLYoEIAhIdxYsn0Hael8PfYTbirBrvo6QR&index=5&pp=iAQB', 1);

--curso 2
INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Primeros reyes persas', 'Los primeros reyes', TRUE, NULL,
'https://www.youtube.com/watch?v=WtQ_d0lIrt4&list=PLUx8354UG5yyCwKAnaWFM3q0XEEJoDS1G&index=1&pp=iAQB', 2);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('El temprano Medes', 'Medes', TRUE, NULL,
'https://www.youtube.com/watch?v=FypaFjqMY04&list=PLUx8354UG5yyCwKAnaWFM3q0XEEJoDS1G&index=2&pp=iAQB', 2);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Periodo Neo-elamita', 'Nuevo periodo', TRUE, NULL,
'https://www.youtube.com/watch?v=mZ2ibQtICKQ&list=PLUx8354UG5yyCwKAnaWFM3q0XEEJoDS1G&index=3&pp=iAQB', 2);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Ciro el grande', 'El gran rey', TRUE, NULL,
'https://www.youtube.com/watch?v=wMbD7c-YlAE&list=PLUx8354UG5yyCwKAnaWFM3q0XEEJoDS1G&index=4&pp=iAQB', 2);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Cambises II', 'Otro gran rey', TRUE, NULL,
'https://www.youtube.com/watch?v=Nq1H4KHCySE&list=PLUx8354UG5yyCwKAnaWFM3q0XEEJoDS1G&index=5&pp=iAQB', 2);

--curso 3
INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Los reyes miticos', 'Los inicios', TRUE, NULL,
'https://www.youtube.com/watch?v=ItwGz43a_ak&list=PLmhKTejvqnoOrQOcTY-pxN00BOZTGSWc3&index=1&pp=iAQB', 3);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('La republica', 'La republica romana', TRUE, NULL,
'https://www.youtube.com/watch?v=plm9DvpInyY&list=PLmhKTejvqnoOrQOcTY-pxN00BOZTGSWc3&index=2&pp=iAQB', 3);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('La republica II', 'La nueva republica romana', TRUE, NULL,
'https://www.youtube.com/watch?v=FZvaOg4RKHQ&list=PLmhKTejvqnoOrQOcTY-pxN00BOZTGSWc3&index=3&pp=iAQB', 3);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Primera guerra Punica', 'Guerra contra Cartago', TRUE, NULL,
'https://www.youtube.com/watch?v=1jWwlS879kY&list=PLmhKTejvqnoOrQOcTY-pxN00BOZTGSWc3&index=4&pp=iAQB', 3);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Segunda guerra Punica', 'Segunda guerra contra Cartago', TRUE, NULL,
'https://www.youtube.com/watch?v=XRXEdv7Dxkg&list=PLmhKTejvqnoOrQOcTY-pxN00BOZTGSWc3&index=5&pp=iAQB', 3);


--curso 4
INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Ascenso a la gloria', 'Inicios de Venecia', TRUE, NULL,
'https://www.youtube.com/watch?v=cZjsO8p9FlU&list=PLhef45iXo5mWJeoQJUWIily8gNmV8GjmD&index=1&pp=iAQB', 4);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('¿Por qué en el agua?', 'Explicación', TRUE, NULL,
'https://www.youtube.com/watch?v=DSEmEHwjVOs&list=PLhef45iXo5mWJeoQJUWIily8gNmV8GjmD&index=2&pp=iAQB', 4);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('¿Por qué nadie vive en Venecia?', 'La poblacion de Venecia', TRUE, NULL,
'https://www.youtube.com/watch?v=SClC9TtQlco&list=PLhef45iXo5mWJeoQJUWIily8gNmV8GjmD&index=3&pp=iAQB', 4);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Venecia explicada', 'Como realmente funciona Venecia', TRUE, NULL,
'https://www.youtube.com/watch?v=e6QYsMvRbDk&list=PLhef45iXo5mWJeoQJUWIily8gNmV8GjmD&index=4&pp=iAQB', 4);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('La republica de Venecia', 'Como realmente funciona Venecia', TRUE, NULL,
'https://www.youtube.com/watch?v=7cHK4xzAhzE&list=PLhef45iXo5mWJeoQJUWIily8gNmV8GjmD&index=5&pp=iAQB', 4);

--curso 5
INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('La leyenda Negra', 'Que hay realmente detras de la leyenda negra estadounidense?', TRUE, NULL,
'https://www.youtube.com/watch?v=6E9WU9TGrec&list=PL8dPuuaLjXtMwmepBjTSG593eG7ObzO7s&index=2&pp=iAQB', 5);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Dia de accion de gracias', 'Costumbre de la epoca colonial', TRUE, 'C:\MediaTemp\pdfs\sample-1.pdf',
'https://www.youtube.com/watch?v=o69TvQqyGdg&list=PL8dPuuaLjXtMwmepBjTSG593eG7ObzO7s&index=3&pp=iAQB', 5);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('La leyenda Negra', 'Que hay realmente detras de la leyenda negra estadounidense?', TRUE, NULL,
'https://www.youtube.com/watch?v=6E9WU9TGrec&list=PL8dPuuaLjXtMwmepBjTSG593eG7ObzO7s&index=2&pp=iAQB', 5);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Nativos y colonizadores', 'Choque de mundos', TRUE, NULL,
'https://www.youtube.com/watch?v=TTYOQ05oDOI&list=PL8dPuuaLjXtMwmepBjTSG593eG7ObzO7s&index=4&pp=iAQB', 5);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('La guerra de los 7 años', 'polvora para la revolucion', TRUE, NULL,
'https://www.youtube.com/watch?v=5vKGU3aEGss&list=PL8dPuuaLjXtMwmepBjTSG593eG7ObzO7s&index=6&pp=iAQB', 5);

--curso 6
INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Hijos del sol', 'Los pueblos indigenas', TRUE, NULL,
'https://www.youtube.com/watch?v=1Iwf02w80H8&list=PLkarkpW5fDPuDeRD6Ff-D0gEjwxes4otL&index=1&pp=iAQB', 6);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Mas alla de los Andes', 'Explorando mas territorios', TRUE, NULL,
'https://www.youtube.com/watch?v=15aWP0jDbvg&list=PLkarkpW5fDPuDeRD6Ff-D0gEjwxes4otL&index=2&pp=iAQB', 6);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Constitucion', 'La primera constitucion', TRUE, NULL,
'https://www.youtube.com/watch?v=HwGoSYXk9uI&list=PLkarkpW5fDPuDeRD6Ff-D0gEjwxes4otL&index=3&pp=iAQB', 6);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Los caminos al mar', 'La guerra del pacifico', TRUE, NULL,
'https://www.youtube.com/watch?v=hjAeijum1BM&list=PLkarkpW5fDPuDeRD6Ff-D0gEjwxes4otL&index=4&pp=iAQB', 6);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('La guerra federal', 'Guerra federal', TRUE, NULL,
'https://www.youtube.com/watch?v=3YsetEd2HSw&list=PLkarkpW5fDPuDeRD6Ff-D0gEjwxes4otL&index=5&pp=iAQB', 6);

-- curso 7
INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Introduccion', 'Comencemos el viaje', TRUE, NULL,
'https://www.youtube.com/watch?v=X393RFZe9PQ&list=PLST0MQhigVdYP5v3Xw1mpIKgI74oJdqKp&index=1&pp=iAQB', 7);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Mexico Prehispanico', 'Viaje antes de la colonia', TRUE, NULL,
'https://www.youtube.com/watch?v=eWVBA0bC8WU&list=PLST0MQhigVdYP5v3Xw1mpIKgI74oJdqKp&index=2&pp=iAQB', 7);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Mexico Colonial', 'EL mexico colonial', TRUE, NULL,
'https://www.youtube.com/watch?v=_AUsXp9TPhw&list=PLST0MQhigVdYP5v3Xw1mpIKgI74oJdqKp&index=3&pp=iAQB', 7);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('La guerra de la independencia', 'Grito libertario', TRUE, NULL,
'https://www.youtube.com/watch?v=653AVoiLN9Q&list=PLST0MQhigVdYP5v3Xw1mpIKgI74oJdqKp&index=4&pp=iAQB', 7);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('La revolucion mexicana', 'Grito libertario', TRUE, NULL,
'https://www.youtube.com/watch?v=EW4_Xk8pROE&list=PLST0MQhigVdYP5v3Xw1mpIKgI74oJdqKp&index=5&pp=iAQB', 7);

-- curso 8
INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('El nacimiento de una lengua', 'Inicios del inglés', TRUE, NULL,
'https://www.youtube.com/watch?v=K1XQx9pGGd0&list=PLV50II2XzmY-9GLZWAuieOp27mZUQfKnj&index=1&pp=iAQB', 8);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('La aventura del inglés', 'Inicios del inglés', TRUE, NULL,
'https://www.youtube.com/watch?v=DG7REAOG1kc&list=PLV50II2XzmY-9GLZWAuieOp27mZUQfKnj&index=2&pp=iAQB', 8);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('La batalla del lenguaje de la biblio', 'La biblia inglesa', TRUE, NULL,
'https://www.youtube.com/watch?v=3cZR1EXGapc&list=PLV50II2XzmY-9GLZWAuieOp27mZUQfKnj&index=3&pp=iAQB', 8);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Esta tierra y este reino', 'Los territorios ingleses', TRUE, NULL,
'https://www.youtube.com/watch?v=1Kg63k5JDH8&list=PLV50II2XzmY-9GLZWAuieOp27mZUQfKnj&index=4&pp=iAQB', 8);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('El inglés en America', 'La lengua colonial', TRUE, NULL,
'https://www.youtube.com/watch?v=oBqlVl0K9tw&list=PLV50II2XzmY-9GLZWAuieOp27mZUQfKnj&index=5&pp=iAQB', 8);

--curso 9
INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Computes Science', 'Los inicios', TRUE, NULL,
'https://www.youtube.com/watch?v=tpIctyqH29Q&list=PLIQNwgNJoeihYT642PFHtKS4-VUsVcYYc&index=1&pp=iAQB', 9);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('La computacion temprana', 'Los inicios de la computacion', TRUE, NULL,
'https://www.youtube.com/watch?v=O5nskjZ_GoI&list=PLIQNwgNJoeihYT642PFHtKS4-VUsVcYYc&index=2&pp=iAQB', 9);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('La electronica', 'La electronica y computacion', TRUE, NULL,
'https://www.youtube.com/watch?v=LN0ucKNX0hc&list=PLIQNwgNJoeihYT642PFHtKS4-VUsVcYYc&index=3&pp=iAQB', 9);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Logica Booleana', 'Algebra de Bool', TRUE, NULL,
'https://www.youtube.com/watch?v=gI-qXk7XojA&list=PLIQNwgNJoeihYT642PFHtKS4-VUsVcYYc&index=4&pp=iAQB', 9);

--curso 10
INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Grecia', 'Los inicios de la filosofia', TRUE, NULL,
'https://www.youtube.com/watch?v=Yat0ZKduW18&list=PL9GwT4_YRZdBf9nIUHs0zjrnUVl-KBNSM&index=1&pp=iAQB', 10);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('El universo moral', 'Un concepto importante', TRUE, NULL,
'https://www.youtube.com/watch?v=c2dyP-OtruM&list=PL9GwT4_YRZdBf9nIUHs0zjrnUVl-KBNSM&index=2&pp=iAQB', 10);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('Los sofistas griegos', '', TRUE, NULL,
'https://www.youtube.com/watch?v=yP3iSIszLeA&list=PL9GwT4_YRZdBf9nIUHs0zjrnUVl-KBNSM&index=3&pp=iAQB', 10);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('La epistemologia de Platon', 'Platon el Strongman', TRUE, NULL,
'https://www.youtube.com/watch?v=5xVakHLDxAc&list=PL9GwT4_YRZdBf9nIUHs0zjrnUVl-KBNSM&index=4&pp=iAQB', 10);

INSERT INTO tbl_lectures (title, description, is_video, file_path, link, course_id)
VALUES ('La teoria de las formas de Platon', 'Platon el Strongman y su teorias de las formas', TRUE, NULL,
'https://www.youtube.com/watch?v=CClQSBvRszI&list=PL9GwT4_YRZdBf9nIUHs0zjrnUVl-KBNSM&index=5&pp=iAQB', 10);


-- INSERT RELATIONSHIPS
INSERT INTO tbl_user_enrolled_in_course VALUES (1, 1);
INSERT INTO tbl_user_takes_lecture VALUES (1, 1);


-- SHOW RESULTS
SELECT * FROM tbl_users tu;
SELECT * FROM tbl_administrators ta;
SELECT * FROM tbl_categories tc;
SELECT * FROM tbl_courses tc;
SELECT * FROM tbl_lectures tl ORDER BY course_id, order_num;
SELECT * FROM tbl_user_enrolled_in_course tueic;
SELECT * FROM tbl_user_takes_lecture tutl;
