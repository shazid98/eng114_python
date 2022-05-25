
class Money:
    def __init__(self, amount):
        self.amount = amount

    def format(self, format_spec):
        if format_spec == "£":
            return f"£{self.amount:.2f}"
        else:
            return f"£{0}"


# value = Money(20)
# #
# print(value.format("£"))
