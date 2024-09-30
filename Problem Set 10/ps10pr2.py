#
# ps10pr2.py (Problem Set 10, Problem 2)
# Date: 8/6/24
# Name: Benjamin Kim
# email: benjt@bu.edu
# Description: A Connect Four Player class. 


from ps10pr1 import Board

# Write your class below.
class Player:
    '''a blueprint for objects that represent Connect Four players.
    '''
    def __init__(self, checker):
        '''the Player constructor'''
        
        ##Validates the inputs for the parameter.
        assert(checker == 'X' or checker == 'O')
        
        #Initialize the data members.
        self.checker = checker
        self.num_moves = 0
    
    def __repr__(self):
        '''returns a string representation for a Player object'''
        return 'Player ' + self.checker

    def opponent_checker(self):
        '''returns a one-character string representing the checker of the 
        Player object’s opponent.
        '''
        
        #If the player's checker is X, return O. If O, return X.
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

    def next_move(self, b):
        '''returns the column where the player wants to make the next move.'''
        
        #The player's input gets saved to the column variable.
        column = int(input('Enter a column: '))
        
        #If it's possible to add a checker to that column, increment num_moves
        #by 1 and return column.
        if b.can_add_to(column) == True:
            self.num_moves += 1
            return column
        
        #If it's not, keep asking for inputs until it is.
        else:
            while b.can_add_to(column) == False:
                column = int(input('Invalid input. Try again: '))
        
        #In case of multiple inputs, ensures the method will increment 
        #num_moves by 1 and return column when it breaks out of the else
        #part of the if statement.
        self.num_moves += 1
        return column
        
if __name__ == '__main__':
    
    #Test to ensure the class works.
    p = Player('X')
    print(p)
    
    #opponent_checker test case.
    print(p.opponent_checker())
    
    #next_move test case.
    b1 = Board(6, 7)    # valid column numbers are 0 - 6
    print(p.next_move(b1))
    print(b1)