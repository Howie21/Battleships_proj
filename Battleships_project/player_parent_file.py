
from array import *

class Player:
    def __init__(self, name, board_size):
        self.name = name 
        self.board_size = board_size
        self.ships = []
        self.score = 0
        self.ocean = ['O']
        self.hit = ['X']
        self.miss = ['M']
        self.been_hit = ["F"]
        self.enemy_miss = ['E']   
        self.players_board = []
        self.players_radar = []
        self.create_boards()
    
    def place_ships(self):
        pass 

    def print_player_board(self):
        board_name = 'YourGameBoard'
        divider = "____________________"
        print()
        for letter in board_name:
            print(letter, end = " ")
        print()
        for letter in divider:
            print(letter, end = " ")
        print()
        for position in self.players_board:
            for c in position:
                if c != '10':
                    print(c, end = "   ")
                elif c == '10':
                    print(c, end = "  ")
            print()
        print()

    def print_player_radar(self):
        board_name = 'YourAirRADAR'
        divider = "____________________"
        for letter in board_name:
            print(letter, end = " ")
        print()
        for letter in divider:
            print(letter, end = " ")
        print()
        for position in self.players_radar:
            for c in position:
                if c != '10':
                    print(c, end = "   ")
                elif c == '10':
                    print(c, end = "  ")
            print()
        print()

    def create_boards(self,):
        for num in range(self.board_size + 1):
            self.players_board.append(['O'] * (self.board_size + 1))
        for num in range(self.board_size + 1):
            self.players_radar.append(['O'] * (self.board_size + 1))
        self.label_board(self.players_board)
        self.label_board(self.players_radar)


    def label_board(self, board_name):
        counter = 0
        counter2 = 0
        for index in range(len(board_name)):
            board_name[index][0] = str(counter)
            counter += 1
        for index in range(len(board_name)):
            board_name[0][index] = str(counter2)
            counter2 += 1
    
    def show_boards(self):
        self.print_player_board()
        self.print_player_radar()

    