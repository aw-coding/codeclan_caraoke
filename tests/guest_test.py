import unittest
from src.guest import Guest
from src.room import Room


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

    def test_customer_paid_entry_fee(self):
        small_room = Room("Small Room", 3, 20)
        self.frank.pay_room_entry_fee(small_room.entry_fee)
        self.assertEqual(10, self.frank.wallet)

    def test_customer_cannot_afford_entry_fee(self):
        vip_room = Room("VIP Room", 8, 50)
        self.assertEqual("Frank cannot afford this" , self.frank.pay_room_entry_fee(vip_room.entry_fee))
