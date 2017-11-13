DROP database IF EXISTS fuzz;
create database fuzz;

DROP TABLE IF EXISTS fuzz.Phone_Event;
CREATE TABLE fuzz.Phone_Event (
	type TINYINT,
    time DATETIME
);
