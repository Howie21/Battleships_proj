
from array import *

class Player:
    def __init__(self, name):
        self.name = name
        self.ships = []
        self.score = 0
        self.ocean = ['-']
        self.hit = ['X']
        self.miss = ['O']
        self.players_board = []
        self.players_radar = []
    
    def place_ships(self):
        pass 

    def print_player_board(self):
        for position in self.players_board:
            for c in position:
                print(c, end = " ")

    def print_player_radar(self):
        for position in self.players_radar:
            for c in position:
                print(c, end = " ")

    def create_board(self, board_size, board):
        for num in range(board_size):
            board.append(['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'])
