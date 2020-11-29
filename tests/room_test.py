import unittest

from src.room import Room
from src.song import Song
from src.guest import Guest


#Room(name, setlist[], capacity, current occupants[])

class TestRoom(unittest.TestCase):
    def setUp(self): #setUp can only contain Room objects!
        self.large_room = Room("Large Room", 5)
        self.small_room = Room("Small Room", 3)
        self.vip_room = Room("VIP Room", 8)


    def test_room_has_name(self):
        self.assertEqual("Large Room", self.large_room.name)

    def test_room_has_capacity(self):
        self.assertEqual(5, self.large_room.capacity)

    def test_add_song_to_room_set_list(self):
        song_1 = Song("Move on Up")
        self.small_room.add_song_to_set_list(song_1)
        self.assertEqual("Move on Up", self.small_room.set_list[0].name)

    def test_add_three_songs_to_set_list(self):
        song_1 = Song("Move on Up")
        song_2 = Song("I Want To Break Free")
        song_3 = Song("Africa")
        self.small_room.add_song_to_set_list(song_1)
        self.small_room.add_song_to_set_list(song_2)
        self.small_room.add_song_to_set_list(song_3)
        self.assertEqual([song_1, song_2, song_3], self.small_room.set_list)

    def test_check_guest_into_room(self):
        alice =        Guest("Alice", 75)

        self.small_room.check_guest_into_room(alice)
        self.assertEqual("Alice", self.small_room.current_occupants[0].name)

    def test_if_room_is_fully_occupied(self):
        alice =        Guest("Alice", 75)
        bob =          Guest("Bob", 60)
        candice =      Guest("Candice", 55)
        danny =        Guest("Danny", 75)
        emily =        Guest("Emily", 60)
        frank =        Guest("Frank", 30)

        self.small_room.check_guest_into_room(alice)
        self.small_room.check_guest_into_room(bob)
        self.small_room.check_guest_into_room(candice)
        self.assertEqual("Sorry, Emily, that room is full.", self.small_room.check_guest_into_room(emily))

    def test_if_guest_is_checked_out(self):
        alice =        Guest("Alice", 75)
        self.small_room.check_guest_into_room(alice)
        self.small_room.check_guest_out_of_room(alice)
        self.assertEqual(0, len(self.small_room.current_occupants))

    def test_if_room_cleared(self):
        alice =        Guest("Alice", 75)
        bob =          Guest("Bob", 60)
        candice =      Guest("Candice", 55)

        self.small_room.check_guest_into_room(alice)
        self.small_room.check_guest_into_room(bob)
        self.small_room.check_guest_into_room(candice)
        self.small_room.remove_all_guests()
        self.assertEqual(0, len(self.small_room.current_occupants))
        
        
        







