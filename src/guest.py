class Guest():
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def pay_room_entry_fee(self, entry_fee):
        if self.wallet >= entry_fee:
            self.wallet -= entry_fee        
        else:
            return f"{self.name} cannot afford this"


        