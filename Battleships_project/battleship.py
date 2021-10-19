
from Ship_ParentClass import Ship

class Battleship(Ship):
    def __init__(self, name):
        self.name = name
        self.space_size = 4
        self.identifier = ['B']
        super.__init__()