
from Ship_ParentClass import Ship

class AirCraft_Carrier(Ship):
    def __init__(self, name):
        self.name = name
        self.space_size = 5
        self.identifier = 'A'
        super.__init__()