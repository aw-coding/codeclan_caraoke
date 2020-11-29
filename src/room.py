


class Room():
    def __init__(self, name, capacity):
        self.name = name
        self.set_list = []
        self.capacity = capacity
        self.current_occupants = []


    def add_song_to_set_list(self, item):
        self.set_list.append(item)

    def check_guest_into_room(self, guest):
        if len(self.current_occupants) < self.capacity:
            self.current_occupants.append(guest)
        else:
            return f"Sorry, {guest.name}, that room is full."

    def check_guest_out_of_room(self, guest):
        self.current_occupants.remove(guest)