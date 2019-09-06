CREATE TABLE flights(
	id SERIAL PRIMARY KEY,
	origin VARCHAR NOT NULL,
	destination VARCHAR NOT NULL,
	duration INTEGER NOT NULL
);

INSERT INTO flights (origin, destination, duration)
VALUES('New York','London',415);

INSERT INTO flights (origin, destination, duration)
VALUES('Guatemala','Rusica',999);

#psql lecture33

# \d


# SELECT * FROM flights where id = 1;

# SELECT MIN(duration) FROM flights; 

# SELECT * FROM flights WHERE origin LIKE '%a%';

SELECT COUNT(*) FROM flights;


UPDATE flights SET duration = 430 WHERE origin = 'New York'
AND destination = 'London';

# DELETE FROM countries WHERE destination = 'Tokyo';


