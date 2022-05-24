class Dog:

    def __init__(self, name, colour):       # Constructor
        self.animal_kind = "canine"
        self.name = name
        self.colour = colour
        self.bark()

    def bark(self):
        return "woof"


fido = Dog("fido", "brown")

print(fido.name)
print(fido.colour)
