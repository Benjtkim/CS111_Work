#
# ps10pr3.py (Problem Set 10, Problem 3)
#
# Date: 8/6/24
# Name: Benjamin Kim
# email: benjt@bu.edu
# Description: Playing the game

from ps10pr1 import Board
from ps10pr2 import Player
import random

def process_move(p, b):
    '''performs all of the steps involved in processing a single move by 
    player p on board b.
    '''
    #Tells us whose turn it is.
    print(str(p) + "\'s", 'turn.')
    
    #The player's next move.
    player_next_move = p.next_move(b)
    
    #Performs that next move to the board.
    b.add_checker(p.checker, player_next_move)
    
    #Print an empty line and then the modified board.
    print('\n')
    print(b)
    
    #If the player wins, print the following line and then True.
    if b.is_win_for(p.checker) == True:
        print(p, 'wins in ', p.num_moves, ' moves.' + '\n', 'Congratulations!')
        return True
    
    #If it's a tie, print the following line and then true.
    elif (b.is_win_for(p.checker) == True and 
          b.is_win_for(p.opponent_checker) == True):
        print("It's a tie!")
        return True
    
    #If it's neither a win or a tie, return False.
    else:
        return False

def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One player should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure one player is 'X' and one is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board):
            return board

        if process_move(player2, board):
            return board
        
if __name__ == '__main__':
    
    b1 = Board(2, 4)
    b1.add_checkers('001122')
    print(b1)
    process_move(Player('X'), b1)
    
