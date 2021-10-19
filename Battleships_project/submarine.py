from Ship_ParentClass import Ship


class Submarine(Ship):
    def __init__(self, name):
        self.name = name
        self.space_size = 3
        self.identifier = ['S']