from Ship_ParentClass import Ship
from aircraft_carrier import AirCraft_Carrier
from battleship import Battleship
from submarine import Submarine
from destroyer import Destroyer
from player_parent_file import Player


class Gameboard:
    def __init__(self):
        self.name = 'The Pacific Ocean'
        self.test_player = Player('The Captain', 10)
    
    
    board_size = input('Please input a board size decided on by both players!: ')    
    player_1 = Player("Player 1", board_size)
    player_2 = Player("Player 2", board_size)  

    def display_welcome(self):
        print('\nWelcome to Battleships!!!')
        print('\nFor you players that may have not played before, let me explain to you how the game works!')
        print(f'\nThis is what the game boards looks like!: ')
        self.test_player.show_boards()
        print('Each player is given their gameboard, this is where you will see where your ships are and where the enemy has hit!\nEach player is also given a Radar Board to keep track of where they have guessed and missed, hit')
        self.legend()


    def legend(self):
        print(F'Below is the Game Legend of symbols and what they stand for!')
        print(f'{self.test_player.ocean} represents the Ocean\n{self.test_player.hit} represents a Hit\n{self.test_player.been_hit} represents a space where the enemy has hit you!\n{self.test_player.miss} represents a shot fired where you missed\n{self.test_player.enemy_miss} respresents a spot which the enemy fired and missed!\n ')
        print("'S' is for Submarine;\n'D' is for Destroyer;\n'A' is for AirCraft Carrier;\n'B' is for BattleShip;")

    def battleships(self):

        pass

    def run_game(self):
        self.display_welcome()
        self.battleships()

    