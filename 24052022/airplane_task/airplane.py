from aircraft import Aircraft


class Airplane(Aircraft):

    def __init__(self):
        super().__init__()
        self.company = "BA"
        self.capacity = 200
        self.flights = []

    def check_flights(self):
        return self.flights






