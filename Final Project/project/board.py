 #
# board.py (Final project)
#
# Description: A Board class for the Eight Puzzle
# Date: 8/10/24
# Name: Benjamin Kim 
# email: benjt@bu.edu

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[0] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        #Loops through each tile and sets the value of each tile
        #to digistr[3 * r + c].
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                self.tiles[r][c] = int(digitstr[3 * r + c])
                
                #If digistr[3  * r + c] is 0, set blank_r to r and blank_c
                #to c.
                if int(digitstr[3 * r + c]) == 0:
                    self.blank_r = r
                    self.blank_c = c

    ### Add your other method definitions below. ###

    def __repr__(self):
        '''returns a string representation of a Board object'''
        #Begin with an empty string.
        s = ''
        
        #Loops through each tile and concatenates a string version of the 
        #value of that tile along with a space to s, unless the value is 0.
        for r in range(len(self.tiles)):   
            for c in range(len(self.tiles[0])):
                
                #In that case, it concatenates a hyphen along with a space.
                if self.tiles[r][c] == 0:
                    s += '_' + ' '
                else:
                    s += str(self.tiles[r][c]) + ' '
        
            s += '\n'  # Newline at the end of the row
        
        return s
    
    def move_blank(self, direction):
        '''takes a string direction that specifies the direction in which the 
        blank should move, and attempts to modify the contents of the called 
        Board object accordingly.'''
        #Checks to ensure direction is a valid input.
        if (direction != 'up' and direction != 'down' and direction != 'left'
            and direction != 'right'):
            return False
        
        #The following chunk of code initializes local variables for the 
        #coordinates the moved blank space will have. If it's moved up, 
        #new_r will be blank_r - 1. If moved down, new_r will be 
        #blank_r + 1. If moved left, new_c will be blank_c - 1. And if 
        #moved right, new_c will be blank_c + 1.
        if direction == 'up':
            new_r = self.blank_r - 1
            new_c = self.blank_c
        elif direction == 'down':
            new_r = self.blank_r + 1
            new_c = self.blank_c
        elif direction == 'left':
            new_r = self.blank_r
            new_c = self.blank_c - 1
        elif direction == 'right':
            new_r = self.blank_r
            new_c = self.blank_c + 1
            
        #If either of the new coordinates is out of bounds, the function 
        #returns False.
        if (new_r > len(self.tiles) - 1 or new_c > len(self.tiles[0]) - 1 
            or new_r < 0 or new_c < 0):
            return False
        
        #Else, move the blank space to self.tiles[new_r][new_c] and
        #the number that was originally there to self.tiles[blank_r][blank_c].
        else:
            moved_number = self.tiles[new_r][new_c]
            self.tiles[new_r][new_c] = 0
            self.tiles[self.blank_r][self.blank_c] = moved_number
            self.blank_r = new_r
            self.blank_c = new_c
            return True

    def digit_string(self):
        '''returns a string of digits that corresponds to the current 
        contents of the called Board object’s tiles attribute.'''
        #Begin with an empty string.
        s = ''
        
        #For loop that loops through each tile and concatenates a string
        #version of the value of that tile to s.
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                s += str(self.tiles[r][c])
                
        return s
    
    def copy(self):
        '''returns a newly-constructed Board object that is a deep copy of 
        the called object'''
        #Varible for the digits that will be used for the copy
        digits = self.digit_string()
        
        #The copy will be saved onto this variable.
        board_copy = Board(digits)
        
        return board_copy

    def num_misplaced(self):
        '''returns the number of tiles in the called Board object that are 
        not where they should be in the goal state.'''
        #This result variable will eventually be subtracted by 1 and then 
        #returned to give the answer.
        result = 0
        
        #This count variable will be increased by 1 for each tile
        #that's iterated over.
        count = 0
        
        #For loop that iterates through all the tiles.
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                
                #If the value of the tile is the same as count, 
                #only count will increase.
                if self.tiles[r][c] == count:
                    count += 1
                    
                #If not, both result and count will increase.
                else:
                    result += 1
                    count += 1

        return result - 1
    
    def return_coordinates(self, value):
        '''returns where the specified value is in self.tiles.'''
        #For each tile in self.tiles, if its value matches value, 
        #return its coordinates as a list.
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] == value:
                    return [r, c]
    
    def total_distance(self):
        '''returns the sum of the distances of each tile from its
        goal position.'''
        #This result variable will eventually be subtracted by 1 and then 
        #returned to give the answer.
        result = 0
        
        #This count variable will be increased by 1 for each tile
        #that's iterated over.
        count = 0
        
        #For loop that iterates through all the tiles.
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                
                #If the value of the tile is the same as count, 
                #only count will increase.
                if self.tiles[r][c] == count:
                    count += 1
                    
                #Else,
                else:
                    #find where count is in self.tiles, and save its 
                    #coordinates to coordinates,
                    coordinates = self.return_coordinates(count)
                    
                    #and increase count by (coordinates[0] - r) + 
                    #(coordinates[1] - c)
                    result += abs((coordinates[0] - r)) + abs((coordinates[1] - c))
                    count += 1
                    
        return result
    
    def __eq__(self, other):
        '''returns True if the called object and the argument have 
        the same values for the tiles attribute, and False otherwise.'''
        #If the for loop comes across a set of tiles that aren't
        #the same, it will return False.
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] != other.tiles[r][c]:
                    return False
                
        #If it never comes across a set of tiles that aren't the same,
        #it will return True.
        return True
    
if __name__ == '__main__':
    
    #__init__ test cases.
    b = Board('142358607')
    print(b.tiles)
    print(b.blank_r)
    print(b.blank_c)
    
    #__repr__ test case.
    print(b)
    
    
    #move_blank test cases.
    print(b.move_blank('up'))
    print(b)
    print(b.blank_r)
    print(b.blank_c)
    print(b.move_blank('left'))
    print(b)
    print(b.move_blank('left'))
    print(b)
    
    #digit_string test case.
    print(b.digit_string())
    
    #copy test case.
    b2 = Board('142358607')
    print(b2)
    b3 = b2.copy()
    print(b3)
    print(b3.move_blank('up'))
    print(b3)
    print(b2)
    
    #num_misplaced test cases.
    b4 = Board('142358607')
    print(b4.tiles)
    print(b4.num_misplaced())
    b4.move_blank('right')
    print(b4.num_misplaced())
    
    #__eq__ test cases.
    b5 = Board('012345678')
    b6 = Board('012345678')
    print(b5 == b6)
    b6.move_blank('right')
    print(b5 == b6)
    
    #return_coordinates test case.
    b = Board('012378546')
    print(b)
    print(b.total_distance())
    