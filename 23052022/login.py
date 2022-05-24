from datetime import datetime

correct_email = "shazid@outlook.com"
correct_password = "password123"

now = (datetime.now()).strftime("%d/%m/%Y at %H:%M:%S")

cond = True

while cond:
    user_email = input("Please put in your email: ").lower()
    user_password = input("Please put in your password: ")
    if "@" not in user_email:
        print("Your email must have an @ in it. Please try again.")
    elif user_email != correct_email:
        print("Wrong email, please try again.")
    elif user_password != correct_password:
        print("Wrong password, please try again.")
    else:
        print(f"Welcome, you have logged in on {now}")
        cond = False

