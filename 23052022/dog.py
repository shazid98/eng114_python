class Dog:

    breed = "canine"      # variable only exists in this class

    def bark(self):     # method is a function in a class, self refers to its class
        print(self.animal_kind)     # self is the scope, making sure it calls the local scope
        return "woof"


fido = Dog()        # Own entity, creates an instance of an object,so it cannot be overwritten
lassie = Dog()
rex = Dog()
daisy = Dog()
tom = Dog()

fido.breed = "Golden Retriever"
lassie.breed = "German Shepherd"
rex.breed = "Doberman"
daisy.breed = "Jack Russell"


print(fido.breed)
print(lassie.breed)
print(rex.breed)
print(daisy.breed)
print(tom.breed)

