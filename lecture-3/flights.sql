CREATE DATABASE lecture3;
use lecture3;

CREATE TABLE flights(
	id SERIAL PRIMARY KEY,
	origin VARCHAR NOT NULL,
	destination VARCHAR NOT NULL,
	duration INTEGER NOT NULL
);

INSERT INTO flights (origin, destination, duration) VALUES('New York','London',415);

INSERT INTO flights (origin, destination, duration) VALUES('Guatemala','Rusica',999);