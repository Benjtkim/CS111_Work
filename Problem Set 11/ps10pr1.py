# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 09:58:28 2024

Name: Benjamin Kim
email: benjt@bu.edu
Description: The Board class.
"""

class Board:
    '''a blueprint for objects that represent boards from the game Connect
    Four.
    '''
    def __init__(self, height, width):
        '''the Board constructor'''
        #Initialize the data members.
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]
        
    def __repr__(self):
        """ returns a string representation for a Board object."""
        s = ''         # Begin with an empty string.
    
        # Add one row of slots at a time.
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row.
    
            for col in range(self.width):
                s += self.slots[row][col] + '|'
    
            s += '\n'  # Newline at the end of the row
        
        #Adds a hyphen under each vertical bar as well as a newline for 
        #the numbers.
        s += '--' * self.width + '-' + '\n'
        
        #Adds a number in between each hyphen to specify each column.
        for num in range(self.width):
            s += ' ' + str(num) 
    
        return s

    def add_checker(self, checker, col):
        """ adds a checker (either an X or an O) to the specified column."""
        #Validates the inputs for the parameters.
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        
        #In descending order so that the loop begins at the bottom of the 
        #specified column, check each slot to see if it's empty. If it is,
        #put the checker there and break out of the loop.
        for row in range(self.height - 1, -1, -1):
            if self.slots[row][col] == ' ':
                self.slots[row][col] = checker
                break
    
    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'
    
        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)
    
            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def reset(self):
        '''resets the Board object on which it is called by setting all slots 
        to contain a space.
        '''
        #Loops through each slot and sets each to a space.
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] = ' '

    def can_add_to(self, col):
        '''returns True if it is valid to place a checker in the column col 
        on the calling Board object. Otherwise, returns False.
        '''
        #If the specified column doesn't exist, return False.
        if col > self.width -1 or col < 0:
            return False
        
        #In descending order so that the loop begins at the bottom of the 
        #specified column, check each slot to see if it's empty. If it is,
        #return True. 
        for row in range(self.height - 1, -1, -1):
            if self.slots[row][col] == ' ':
                return True
            
        #If none of the slots are empty, return False.
        return False
    
    def is_full(self):
        '''returns True if the called Board object is completely full of 
        checkers, and False otherwise.
        '''
        #Check each slot in the board to see if it's empty. If there is an 
        #empty slot, return False.
        for row in range(self.height):
            for col in range(self.width):
                if self.slots[row][col] == ' ':
                    return False
        
        #If none of the slots are empty, return True.
        return True

    def  remove_checker(self, col):
        '''removes the top checker from column col of the called Board 
        object.
        '''
        #Loop through the specified column. If you find a slot that isn't
        #empty, remove the checker and break.
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                break

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker."""
        #Validates the inputs for the parameter.
        assert(checker == 'X' or checker == 'O')
        
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four slots in this row
                # contain the specified checker.
                if (self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker):
                    return True
    
        # if we make it here, there were no horizontal wins.
        return False

    def is_vertical_win(self, checker):
        '''Checks for a vertical win for the specified checker.'''
        #Validates the inputs for the parameter.
        assert(checker == 'X' or checker == 'O')
        
        for row in range(self.height - 3):
            for col in range(self.width):
                # Check if the below four slots in this column
                # contain the specified checker.
                if (self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker):
                    return True
    
        # if we make it here, there were no vertical wins.
        return False
    
    def is_up_diagonal_win(self, checker):
        '''Checks for an above diagnol win for the specified checker.'''
        #Validates the inputs for the parameter.
        assert(checker == 'X' or checker == 'O')
        
        for row in range(self.height - 3):
            for col in range(self.width):
                # Check if the below four, diagnol slots contain the specified 
                # checker.
                if (self.slots[row][col] == checker and \
                   self.slots[row + 1][col - 1] == checker and \
                   self.slots[row + 2][col - 2] == checker and \
                   self.slots[row + 3][col - 3] == checker):
                    return True
    
        # if we make it here, there were up diagnol wins.
        return False
    
    def is_down_diagonal_win(self, checker):
        '''Checks for an down  diagnol win for the specified checker.'''
        #Validates the inputs for the parameter.
        assert(checker == 'X' or checker == 'O')
        
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                # Check if the below four, diagnol slots contain the specified 
                # checker.
                if (self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker):
                    return True
    
        # if we make it here, there were down diagnol wins.
        return False
    
    def is_win_for(self, checker):
        '''accepts a parameter checker that is either 'X' or 'O', and 
        returns True if there are four consecutive slots containing checker 
        on the board. Otherwise, returns False.'''
        #Validates the inputs for the parameter.
        assert(checker == 'X' or checker == 'O')
        
        #If any of the win conditions are true, return True.
        if (Board.is_horizontal_win(self, checker) == True or 
            Board.is_vertical_win(self, checker) == True or 
            Board.is_up_diagonal_win(self, checker) == True or 
            Board.is_down_diagonal_win(self, checker) == True):
            return True
        
        #Else, return False.
        return False
            
if __name__ == '__main__':
    
    #add_checker test cases.
    b = Board(6, 7)
    b.add_checker('X', 0)
    b.add_checker('O', 0)
    print(b)
    
    #reset test case.
    b.reset()
    print(b)
    
    #can_add_to test cases.
    b1 = Board(2, 4)
    b1.add_checkers('001122')
    print(b1)
    print(b1.can_add_to(3))
    print('---------')
    
    #is_full test case.
    b2 = Board(2, 2)
    print(b2.is_full())
    b2.add_checkers('0011')
    print(b2)
    print(b2.is_full())
    print('---------')
    
    #remove_checker test cases.
    b3 = Board(2, 2)
    b3.add_checkers('0011')
    print(b3)
    b3.remove_checker(1)
    print(b3)
    b3.remove_checker(1)
    print(b3)
    b3.remove_checker(1)     # column empty; no effect
    b3.remove_checker(0)
    print(b3)
    print('---------')
    
    #is_horizontal_win test case.
    b4 = Board(5, 5)
    b4.add_checker('X', 0)
    b4.add_checker('X', 1)
    b4.add_checker('X', 2)
    b4.add_checker('X', 3)
    print(b4)
    print(b4.is_horizontal_win('X'))
    print('---------')
    
    #is_vertical_win test case.
    b5 = Board(5, 5)
    b5.add_checker('X', 0)
    b5.add_checker('X', 0)
    b5.add_checker('X', 0)
    b5.add_checker('X', 0)
    print(b5)
    print(b5.is_vertical_win('X'))
    print('---------')
    
    #is_up_diagonal_win test case.
    b6 = Board(5, 5)
    b6.add_checker('X', 1)
    b6.add_checker('O', 2)
    b6.add_checker('X', 2)
    b6.add_checker('O', 3)
    b6.add_checker('O', 3)
    b6.add_checker('X', 3)
    b6.add_checker('O', 4)
    b6.add_checker('O', 4)
    b6.add_checker('O', 4)
    b6.add_checker('X', 4)
    print(b6)
    print(b6.is_up_diagonal_win('X'))
    print('---------')
    
    #is_down_diagonal_win test case.
    b7 = Board(5, 5)
    b7.add_checker('X', 0)
    b7.add_checker('O', 0)
    b7.add_checker('X', 0)
    b7.add_checker('O', 0)
    b7.add_checker('X', 0)
    b7.add_checker('O', 1)
    b7.add_checker('X', 1)
    b7.add_checker('O', 1)
    b7.add_checker('X', 1)
    b7.add_checker('X', 2)
    b7.add_checker('X', 2)
    b7.add_checker('X', 2)
    b7.add_checker('O', 3)
    b7.add_checker('X', 3)
    print(b7)
    print(b7.is_down_diagonal_win('X'))
    print('---------')
    
    #is_win_for test cases.
    b8 = Board(6, 7)
    b8.add_checkers('00102030')
    print(b8)
    print(b8.is_win_for('X'))
    print(b8.is_win_for('O'))
    b9 = Board(6, 7)
    b9.add_checkers('23344545515')
    print(b9)
    print(b9.is_win_for('X')) 
    print(b9.is_win_for('O')) 