import math
class Money:
    def __init__(self, amount):
        self.amount = amount

    def __format__(self, format_spec):
        if format_spec == "2dp":
            return f"Your value is £{self.amount:.2f}"
        else:
            return f"Your balance is £0"


value = Money(100000000000000000000000000000000)
print(f"{value:2dp}")
