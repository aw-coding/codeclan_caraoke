import unittest
from src.guest import Guest


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.alice =        Guest("Alice", 75)
        self.bob =          Guest("Bob", 60)
        self.candice =      Guest("Candice", 55)
        self.danny =        Guest("Danny", 75)
        self.emily =        Guest("Emily", 60)
        self.frank =        Guest("Frank", 30)

    def test_customer_has_name(self):
        self.assertEqual("Alice", self.alice.name)

    def test_customer_has_wallet_amount(self):
        self.assertEqual(55, self.candice.wallet)