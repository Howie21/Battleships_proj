from Ship_ParentClass import Ship


class AirCraft_Carrier(Ship):
    def __init__(self, name):
        self.name = name
        self.space_size = 2
        self.identifier = ['D']