


class Room():
    def __init__(self, name, capacity):
        self.name = name
        self.set_list = []
        self.capacity = capacity
        self.current_occupants = []


    def add_song_to_set_list(self, item):
        self.set_list.append(item)