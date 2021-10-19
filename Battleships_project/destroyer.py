from Ship_ParentClass import Ship


class Destroyer(Ship):
    def __init__(self, name):
        self.name = name
        self.space_size = 2
        self.identifier = 'D'
        super.__init__()