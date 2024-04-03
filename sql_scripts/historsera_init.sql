
--CREATION OF THE TABLES

CREATE  TABLE tbl_users ( 
	id                   SERIAL NOT NULL  ,
	username             varchar(20)  NOT NULL  ,
	email                varchar(70)  NOT NULL  ,
	user_password        varchar(12)  NOT NULL  ,
	creation_date        date DEFAULT CURRENT_DATE NOT NULL  ,
	CONSTRAINT pk_tbl_users PRIMARY KEY ( id )
 );

CREATE  TABLE tbl_courses ( 
	course_id            SERIAL  NOT NULL  ,
	course_name                 varchar(100)  NOT NULL  ,
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
	link                 varchar(350)  NOT NULL  ,
	duration_sec         integer    ,
	course_id            integer  NOT NULL  ,
	CONSTRAINT pk_tbl_lectures PRIMARY KEY ( lecture_id )
 );

CREATE  TABLE tbl_administrators ( 
	user_id              integer    
 );

CREATE  TABLE tbl_user_takes_lecture ( 
	user_id              integer  NOT NULL  ,
	lecture_id           integer  NOT NULL  ,
	is_finished          boolean DEFAULT false NOT NULL  ,
	CONSTRAINT pk_tbl_user_takes_course PRIMARY KEY ( user_id )
 );

CREATE  TABLE tbl_user_enrolled_in_course ( 
	user_id              integer  NOT NULL  ,
	course_id            integer  NOT NULL  ,
	CONSTRAINT pk_tbl_user_enrolled_in_course PRIMARY KEY ( user_id )
 );

ALTER TABLE "public".tbl_user_enrolled_in_course ADD CONSTRAINT fk_tbl_user_enrolled_in_course_user_id FOREIGN KEY ( user_id ) REFERENCES "public".tbl_users( id );
ALTER TABLE "public".tbl_user_enrolled_in_course ADD CONSTRAINT fk_tbl_user_enrolled_in_course_course_id FOREIGN KEY ( course_id ) REFERENCES "public".tbl_courses( course_id );
ALTER TABLE "public".tbl_user_takes_lecture ADD CONSTRAINT fk_tbl_user_takes_course FOREIGN KEY ( user_id ) REFERENCES "public".tbl_users( id );
ALTER TABLE "public".tbl_user_takes_lecture ADD CONSTRAINT fk_tbl_user_takes_lecture FOREIGN KEY ( lecture_id ) REFERENCES "public".tbl_lectures( lecture_id );
ALTER TABLE "public".tbl_administrators ADD CONSTRAINT fk_tbl_administrators FOREIGN KEY ( user_id ) REFERENCES "public".tbl_users( id );
ALTER TABLE "public".tbl_lectures ADD CONSTRAINT fk_tbl_lectures_tbl_courses FOREIGN KEY ( course_id ) REFERENCES "public".tbl_courses( course_id );
ALTER TABLE "public".tbl_courses ADD CONSTRAINT fk_tbl_courses_tbl_categories FOREIGN KEY ( category_name ) REFERENCES "public".tbl_categories( category_name );

