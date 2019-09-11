import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE_URL="postgresql://postgres:postgres@localhost/lecture3"

engine = create_engine(DATABASE_URL)
#engine = create_engine(os.getenv("postgres://username:password@localhost:5432/name_of_db"))
db = scoped_session(sessionmaker(bind=engine))

def main():
	flights = db.execute("SELECT origin, destination, duration FROM flights;").fetchall()
	for flight in flights:
		print(f"{flight.origin} to {flight.destination} minutes.")

if __name__ == '__main__':
	main()