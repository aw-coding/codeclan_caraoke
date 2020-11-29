import unittest

from src.room import Room
from src.song import Song


#Room(name, setlist[], capacity, current occupants[])

class TestRoom(unittest.TestCase):
    def setUp(self): #setUp can only contain Room objects!
        self.large_room = Room("Large Room", 5)
        self.small_room = Room("Small Room", 3)
        self.vip_room = Room("VIP Room", 8)

        song_1 = Song("Move on Up")
        self.song_2 = Song("I Want To Break Free")
        self.song_3 = Song("Africa")
        self.song_4 = Song("September")
        self.song_5 = Song("Life on Mars")
        self.song_6 = Song("Virginia Plain")


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


