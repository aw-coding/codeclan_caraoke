class Room():
    def __init__(self, name, set_list, capacity):
        self.name = name
        self.set_list = set_list
        self.capacity = capacity
        self.current_occupants = []