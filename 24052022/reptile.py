from animal import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chambers = [3, 4]
        self.amniotic_eggs = None

    def seek_heat(self):
        print("It's chilly outside, where's the sun or a decent hot spring")

    def hunt(self):
        print("Wait for the prey , then pounce")

    def use_venom(self):
        print("If I've got it, I'm using it")

    def attract_mate_through_scent(self):
        print("I smell good")


# jeremy = Reptile()
# jeremy.eat()
