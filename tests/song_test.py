import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Move on Up")
        self.song_2 = Song("I Want To Break Free")
        self.song_3 = Song("Africa")
        self.song_4 = Song("September")
        self.song_5 = Song("Life on Mars")
        self.song_6 = Song("Virginia Plain")


    def test_song_has_name(self):
        self.assertEqual("September", self.song_4.name)