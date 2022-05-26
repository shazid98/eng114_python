from datetime import datetime
from airplane import Airplane

now = datetime.now()


class Flight(Airplane):

    def __init__(self):
        super().__init__()
        self.date = now
        self.origin = "London"
        self.destination = "Manchester"
        self.passenger_list = []

    def create_flight(self, date, origin, destination):
        self.date = date
        self.origin = origin
        self.destination = destination
        self.flights.append([date, origin, destination])

    def get_flight_details(self):
        return f"Date: {self.date}, Origin: {self.origin}, Destination: {self.destination}"

    def check_passengers(self):
        return self.passenger_list












