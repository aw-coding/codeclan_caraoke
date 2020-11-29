class Room():
    def __init__(self, name, capacity):
        self.name = name
        self.set_list = []
        self.capacity = capacity
        self.current_occupants = []