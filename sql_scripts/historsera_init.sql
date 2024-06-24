
--CREATION OF THE TABLES

CREATE  TABLE tbl_users ( 
	id                   SERIAL NOT NULL  ,
	username             varchar(20)  NOT NULL  ,
	email                varchar(70)  NOT NULL  ,
	user_password        varchar(12)  NOT NULL  ,
	creation_date        date DEFAULT CURRENT_DATE,
	points 				 integer DEFAULT 0,
	title_name 			 varchar(100) DEFAULT NULL,
	CONSTRAINT pk_tbl_users PRIMARY KEY ( id )
 );

CREATE  TABLE tbl_courses ( 
	course_id            SERIAL  NOT NULL  ,
	course_name          varchar(100)  NOT NULL  ,
	author               varchar(50)  NOT NULL  ,
	description          varchar(350)    ,
	ref_image_path       varchar(350)    ,
	category_name        varchar(150)    ,
	CONSTRAINT pk_tbl_courses PRIMARY KEY ( course_id )
 );

CREATE  TABLE tbl_categories ( 
	category_name        varchar(150)  NOT NULL  ,
	CONSTRAINT pk_tbl_categories PRIMARY KEY ( category_name )
 );


CREATE  TABLE tbl_lectures ( 
	lecture_id           SERIAL  NOT NULL  ,
	title                varchar(100)  NOT NULL  ,
	description          varchar(350)  NOT NULL  ,
	is_video             boolean  NOT NULL  ,
	file_path            varchar(350)    ,
	link                 varchar(350),
	order_num 			 integer DEFAULT 0,
	course_id            integer  NOT NULL  ,
	CONSTRAINT pk_tbl_lectures PRIMARY KEY ( lecture_id )
 );

CREATE  TABLE tbl_administrators ( 
	user_id              integer    unique
 );

CREATE TABLE tbl_titles (
	title_name			varchar(100) NOT NULL,
	points_required 	integer NOT NULL DEFAULT 0,
	CONSTRAINT pk_tbl_titles PRIMARY KEY ( title_name )
);

CREATE  TABLE tbl_user_takes_lecture ( 
	user_id              integer  NOT NULL  ,
	lecture_id           integer  NOT NULL  ,
	is_finished          boolean DEFAULT false NOT NULL
 );

CREATE  TABLE tbl_user_enrolled_in_course ( 
	user_id              integer  NOT NULL  ,
	course_id            integer  NOT NULL
 );

----------- TABLE MODIFICATIONS

ALTER TABLE "public".tbl_user_enrolled_in_course ADD CONSTRAINT fk_tbl_user_enrolled_in_course_user_id FOREIGN KEY ( user_id ) REFERENCES "public".tbl_users( id );
ALTER TABLE "public".tbl_user_enrolled_in_course ADD CONSTRAINT fk_tbl_user_enrolled_in_course_course_id FOREIGN KEY ( course_id ) REFERENCES "public".tbl_courses( course_id );
ALTER TABLE "public".tbl_user_takes_lecture ADD CONSTRAINT fk_tbl_user_takes_course FOREIGN KEY ( user_id ) REFERENCES "public".tbl_users( id );
ALTER TABLE "public".tbl_user_takes_lecture ADD CONSTRAINT fk_tbl_user_takes_lecture FOREIGN KEY ( lecture_id ) REFERENCES "public".tbl_lectures( lecture_id );
ALTER TABLE "public".tbl_administrators ADD CONSTRAINT fk_tbl_administrators FOREIGN KEY ( user_id ) REFERENCES "public".tbl_users( id );
ALTER TABLE "public".tbl_lectures ADD CONSTRAINT fk_tbl_lectures_tbl_courses FOREIGN KEY ( course_id ) REFERENCES "public".tbl_courses( course_id );
ALTER TABLE "public".tbl_courses ADD CONSTRAINT fk_tbl_courses_tbl_categories FOREIGN KEY ( category_name ) REFERENCES "public".tbl_categories( category_name );
ALTER TABLE "public".tbl_users ADD CONSTRAINT fk_tbl_users_tbl_titles FOREIGN KEY ( title_name ) REFERENCES "public".tbl_titles ( title_name );

------------------------ REQUIRED TRIGGERS ---------------------------------
-- This trigger is called when a a Lecture is created in order to asign its order_num
CREATE OR REPLACE FUNCTION  sp_LEC_assign_order_num()
RETURNS TRIGGER AS 
$$
DECLARE 
	current_num integer;

BEGIN

	SELECT COUNT(tl.course_id) INTO current_num FROM tbl_lectures tl
	JOIN tbl_courses tc ON tl.course_id = tc.course_id
	WHERE tl.course_id = NEW.course_id	
	GROUP BY tl.course_id;

	IF (current_num IS null) THEN
		NEW.order_num := 1;
		RETURN NEW;
	END IF;

	
	NEW.order_num := current_num + 1;
	RETURN NEW;
	
END
$$
LANGUAGE PLPGSQL;

CREATE OR REPLACE TRIGGER order_num_trigger
BEFORE INSERT ON tbl_lectures
FOR EACH ROW 
EXECUTE FUNCTION sp_LEC_assign_order_num();

-- Cambiar el orden de las lecciones
CREATE OR REPLACE PROCEDURE sp_LEC_change_order_num(
    p_lecture_id integer,
    p_new_order_num integer
)
AS
$$
DECLARE
    v_course_id integer;
    v_old_order_num integer;
   	v_max_order integer;
BEGIN
	
	SELECT MAX(order_num) INTO v_max_order FROM tbl_lectures;
	-- VALIDAR QUE EL nuevo orden sea un numero valido
	IF(p_new_order_num <= v_max_order AND p_new_order_num > 0) THEN
	
	    -- obtiene el id del curso y el numero de orden actual de la leccion
	    SELECT course_id, order_num INTO v_course_id, v_old_order_num
	    FROM tbl_lectures
	    WHERE lecture_id = p_lecture_id;
	
	    -- Se asigna el nuevo orden
	    UPDATE tbl_lectures
	    SET order_num = p_new_order_num
	    WHERE lecture_id = p_lecture_id;
	
	    -- Toca reorganizar las leccioens
	   
	   	IF p_new_order_num = v_old_order_num THEN
	   		RETURN;
	   	END IF;
	   
	    IF p_new_order_num < v_old_order_num THEN
	        -- Si el nuevo orden es menor, aumenta en 1 a las anteriores 
	        UPDATE tbl_lectures
	        SET order_num = order_num + 1
	        WHERE course_id = v_course_id
	        AND lecture_id != p_lecture_id
	        AND order_num >= p_new_order_num
	        AND order_num < v_old_order_num;
	    ELSE
	        -- Si es numero es mayor, le resta 1 a las siguientes
	        UPDATE tbl_lectures
	        SET order_num = order_num - 1
	        WHERE course_id = v_course_id
	        AND lecture_id != p_lecture_id
	        AND order_num <= p_new_order_num
	        AND order_num > v_old_order_num;
	    END IF;
	 ELSE
	 	RAISE EXCEPTION 'Ese nuevo numero de orden no es valido';
	 END IF;
END;
$$
LANGUAGE plpgsql;

------------------- REQUIERED FUNCTIOSN --------
CREATE OR REPLACE FUNCTION get_completion_percent(
	p_user_id int,
	p_course_id int
)
RETURNS INT AS
$$
DECLARE
    total_lectures integer;
    finished_lectures integer;
    completion_percentage numeric;
BEGIN
    -- Get the total number of lectures in the course
    SELECT COUNT(*) INTO total_lectures
    FROM tbl_lectures
    WHERE course_id = p_course_id;

    -- Get the number of lectures finished by the user in the course
    SELECT COUNT(*) INTO finished_lectures
    FROM tbl_user_takes_lecture
    JOIN tbl_lectures ON tbl_user_takes_lecture.lecture_id = tbl_lectures.lecture_id
    WHERE tbl_user_takes_lecture.user_id = p_user_id
      AND tbl_lectures.course_id = p_course_id
      AND tbl_user_takes_lecture.is_finished = true;

    -- Calculate the completion percentage
    IF total_lectures > 0 THEN
        completion_percentage := (finished_lectures::numeric / total_lectures::numeric) * 100;
    ELSE
        completion_percentage := 0;
    END IF;

    RETURN completion_percentage;
END;
$$
LANGUAGE PLPGSQL;


------------- asignar titulo ----------
CREATE OR REPLACE PROCEDURE assign_user_title(p_user_id INT)
AS 
$$
DECLARE
    user_points INT;
    title_to_asign text;
BEGIN
    -- Fetch the user's points based on the given user_id
   SELECT points INTO user_points
   FROM tbl_users
   WHERE id = p_user_id;
   
   SELECT title_name INTO title_to_asign
   FROM tbl_titles tt WHERE points_required <= user_points
   ORDER BY points_required DESC LIMIT 1;

   UPDATE tbl_users SET title_name = title_to_asign
   WHERE id = p_user_id;
END;
$$
LANGUAGE PLPGSQL;
