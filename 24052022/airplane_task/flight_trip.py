from datetime import date as dt
from airplane import Airplane


class Flight:

    def __init__(self, date, origin, destination, price):
        self.date = date
        self.origin = origin
        self.destination = destination
        self.price = price


turkey = Flight("24/05/2022", "London", "Istanbul", 144.5)
