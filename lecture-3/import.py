import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#engine = create_engine(os.getenv("DATABASE_URL"));
# create_engine("postgres://postgres:postgres@localhost:5432/lecture3")

engine = create_engine("postgres://postgres:postgres@localhost:5432/lecture3")
#engine = create_engine(DATABASE_URL)
db = scoped_session(sessionmaker(bind=engine))

def main():
	f = open("flights.csv")
	reader = csv.reader(f)

	for origin, destination, duration in reader:
		db.execute("INSERT INTO flights (origin, destination,duration) VALUES ('Guate',444,33)")
		print(f"Added flight from {origin} to {destination} lasting {duration}")

	db.commit()


if __name__ == '__main__':
	main()