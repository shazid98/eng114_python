name = input("What is your name? ").capitalize()
height = float(input("How tall are you in metres? "))
favourite_colour = input("What is your favourite colour? ").lower()
secrete_spirit_animal = input("What is your secret spirit animal? ").lower()

print(f"Welcome {name}! "
      f"You are {height}m tall and your favourite colour is {favourite_colour}! ")
print(f"The first letter of the spirit animal is {secrete_spirit_animal[0]} "
      f"and the last letter is {secrete_spirit_animal[-1]}")
print(f"The secret animal has {len(secrete_spirit_animal)} letters")

guess = input("What is the secret animal? ").lower()

if guess == secrete_spirit_animal:
    print("Well done! You are correct!")
else:
    print("You got it wrong!")