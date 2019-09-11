import os


from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE_URL="postgresql://postgres:postgres@localhost/lecture3"

engine = create_engine(DATABASE_URL)

db = scoped_session(sessionmaker(bind=engine))

def main():
	# list of flights
	flights = db.execute("SELECT id, origin, destination, duration from flights")
	for flight in flights:
		print(f"Flight {flight.id}: {flight.origin} to {flight.destination}, ")

	#Prompt user to choose a flight 
	flight_id = int(input("\nFlight ID: "))
	flight = db.execute("SELECT origin, destination, duration FROM flights WHERE id = :id", {"id": flight_id}).fetchone()


	# Make sure flight is valid.

	if flight is None:
		print("Error: No such flight.")
		return

		# List passengers.
		passengers = db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id", {"flight_id": flight_id}).fetchall()


		print("\nPassengers: ")
		for passenger in passengers:
			print(passenger.name)
		if len(passengers) == 0:
			print("No passengers.")

