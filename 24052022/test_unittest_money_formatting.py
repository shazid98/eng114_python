from money_formatting import *
import unittest


class Moneytest(unittest.TestCase):

    money = Money(70.4326546)

    # def test_currency(self):
    #     self.assertIn("£", self.money.amount)

    def format(self):
        self.assertEqual(self.money.format("£"), "£70.43")

    





