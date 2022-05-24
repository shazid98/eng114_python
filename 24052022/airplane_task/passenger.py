from flight_trip import Flight


class Passenger:

    def __init__(self, name, surname, passport):
        self.name = name
        self.surname = surname
        self.passport = passport

    def get_passport(self):
        return self.passport

    def buy_flight(self, date, origin, destination):
        Flight.date = date
        Flight.origin = origin
        Flight.destination = destination

    

