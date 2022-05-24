class Animal:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("One breath in and one breath out")

    def eat(self):
        print("Yummy")

    def procreate(self):
        print("Let's find a mate")

    def move(self):
        print("onwards and upwards")


# cat = Animal()
# cat.breathe()