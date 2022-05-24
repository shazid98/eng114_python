
def birthday():
    name = input("What is your name? ").capitalize()
    age = int(input("How old are you? "))
    month = input("What is your birth month? ").capitalize()
    day = int(input(f"What day in {month} were you born in? "))
    accepted_months = ["January", "February", "March", "April", "May"]
    accepted_days = list(range(1, 20))

    if month in accepted_months and day in accepted_days:
        year = 2022 - age
        print(name + ", you were born in " + str(year))
    else:
        year = 2021 - age
        print(name + ", you were born in " + str(year))

birthday()
