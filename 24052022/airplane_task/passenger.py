from flight_trip import Flight


class Passenger(Flight):

    def __init__(self, name, surname, passport):
        super().__init__()
        self.name = name
        self.surname = surname
        self.passport = passport
        self.passenger_details = [name, surname, passport]

    def get_passport(self):
        return self.passport

    def buy_flight(self, date, origin, destination):
        self.date = date
        self.origin = origin
        self.destination = destination
        if len(self.passenger_list) > self.capacity:
            print("Ran out of seats, no more can be sold")
        else:
            self.passenger_list.append(self.passenger_details)      # need to fix this


turkey = Flight()
turkey.create_flight("24/05/2022", "London", "Istanbul")
print(turkey.get_flight_details())
#
eric = Passenger("Eric", "Smith", 6757843)
print(eric.get_passport())
eric.buy_flight(turkey.date, turkey.origin, turkey.destination)
#
print(turkey.check_passengers())

# damian = Passenger("Damian", "Martin", 3948928)






    

