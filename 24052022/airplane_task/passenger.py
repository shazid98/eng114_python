from flight_trip import Flight


class Passenger(Flight):

    def __init__(self, name, surname, passport):
        super().__init__()
        self.name = name
        self.surname = surname
        self.passport = passport
        self.passenger_details = surname + " " + name

    def get_passport(self):
        return self.passport

    def add_passenger(self, passport, passenger):
        self.passenger_list[passport] = passenger

    def buy_flight(self, no, date, origin, destination):
        self.no = no
        self.date = date
        self.origin = origin
        self.destination = destination
        if len(self.passenger_list) > self.capacity:
            return f"Ran out of seats, no more can be sold"
        else:
            self.passenger_list[self.passport] = self.passenger_details      # need to fix this


turkey = Flight()
# <<<<<<< HEAD
# turkey.create_flight("24/05/2022", "London", "Istanbul")
# check_flights()
# print(turkey.get_flight_details())
# #
# #eric = Passenger("Eric", "Smith", 6757843)
# #print(eric.get_passport())
# #eric.buy_flight(turkey.date, turkey.origin, turkey.destination)
# #
# #print(turkey.check_passengers())

# =======
# turkey.create_flight(1234, "24/05/2022", "London", "Istanbul")
# usa = Flight()
# usa.create_flight(1235, "26/05/2022", "London", "New York")

# print(usa.get_flight_details())
# print(turkey.get_flight_details())
# #
# # print(usa.check_flights())


# eric = Passenger("Eric", "Smith", 6757843)
# eric.buy_flight(turkey.no, turkey.date, turkey.origin, turkey.destination)
# eric.add_passenger(6757843, eric)
# print(usa.check_passengers())

# # print(eric.get_passport())
# # eric.buy_flight(turkey.date, turkey.origin, turkey.destination)
# # #
# # print(turkey.check_passengers())
# #
# >>>>>>> bbed7d3bbba46d7612226620dc5e39fc8e024e89
# # damian = Passenger("Damian", "Martin", 3948928)
# # damian.buy_flight(turkey.date, turkey.origin, turkey.destination)
# #
# # print(turkey.check_passengers())






    

