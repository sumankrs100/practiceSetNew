# practiceSetNew

### Below files are used for getting environment value
* dev.env
* prod.env
* test.env

### For running script environment argument is necessary and it should be in ("prod", "dev", "test")
Syntax:
* python main.py -e dev

***

*NOTE: The values for database connection can be passed as argument in case of test environment as mentioned below:*
* python main.py -e test -u {\"db\":\"test_db6\"}
***

### Remember to store DOB in the form of dd/mm/yyyy format

### SQL query to create table in database:

***
create table if not exists public.test_table1
(
	id SERIAL,
	first_name character varying COLLATE pg_catalog."default",
    last_name character varying COLLATE pg_catalog."default",
    dob character varying COLLATE pg_catalog."default",
    sex character varying COLLATE pg_catalog."default",
	creation_time timestamp without time zone default CURRENT_TIMESTAMP,
    CONSTRAINT test_table1_pkey PRIMARY KEY (id)
);
***
