import unittest

from src.room import Room

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.large_room = Room("Large Room", 5)
        self.small_room = Room("Small Room", 3)
        self.vip_room = Room("VIP Room", 8)


    def test_room_has_name(self):
        self.assertEqual("Large Room", self.large_room.name)

    def test_room_has_capacity(self):
        self.assertEqual(5, self.large_room.capacity)


