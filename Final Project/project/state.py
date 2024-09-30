#
# state.py (Final project)
#
# Description: A State class for the Eight Puzzle
# Date: 8/10/24
# Name: Benjamin Kim
# email: benjt@bu.edu

from board import *
from searcher import *

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [[0, 1, 2],
              [3, 4, 5],
              [6, 7, 8]]

# the list of possible moves, each of which corresponds to
# moving the blank cell in the specified direction
MOVES = ['up', 'down', 'left', 'right']

class State:
    """ A class for objects that represent a state in the state-space 
        search tree of an Eight Puzzle.
    """
    ### Add your method definitions here. ###
        
    def __init__(self, board, predecessor, move):
        '''the State constructor.'''
        #Initialize the data attributes.
        self.board = board
        self.predecessor = predecessor
        self.move = move
        
        #If predecessor = None, the num_moves is 0.
        if self.predecessor == None:
            self.num_moves = 0
            
        #If predecessor is not None, num_moves must be 1 more than 
        #the num_moves count of the predecessor.
        else:
            self.num_moves = predecessor.num_moves + 1

    def __repr__(self):
        """ returns a string representation of the State object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = self.board.digit_string() + '-'
        s += self.move + '-'
        s += str(self.num_moves)
        return s
    
    def creates_cycle(self):
        """ returns True if this State object (the one referred to
            by self) would create a cycle in the current sequence of moves,
            and False otherwise.
        """
        # You should *NOT* change this method.
        state = self.predecessor
        while state != None:
            if state.board == self.board:
               return True
            state = state.predecessor
        return False

    def __gt__(self, other):
        """ implements a > operator for State objects
            that always returns True. This will be needed to break
            ties when we use max() on a list of [priority, state] pairs.
            If we don't have a > operator for State objects,
            max() will fail with an error when it tries to compare
            two [priority, state] pairs with the same priority.
        """
        # You should *NOT* change this method.
        return True

    def is_goal(self):
        '''returns True if the called State object is a goal state, and 
        False otherwise.'''
        #State has an attribute called board, which is a board object that
        #itself has an attribute called tiles. Therefore, we must call
        #self.board.tiles. If it matches GOAL_Tiles, return True.
        if self.board.tiles == GOAL_TILES:
            return True
        
        #Else, return False.
        else:
            return False
        
    def generate_successors(self):
        '''returns a list of State objects for all successor states of the 
        called State object.'''
        #The list that will eventually hold all the successor states of the 
        #called State object.
        successors = []
        
        #For each move in MOVES:
        for move in MOVES:
            
            #Create a copy of the board.
            board_copy = self.board.copy()
            
            #Check to see if the move is legal.
            if board_copy.move_blank(move) == True:
                
                #If it is, apply that move and create a new state object for
                #the result of that move.
                new_state = State(board_copy, self, move)
                
                #Finally, append that newly created object to successors.
                successors.append(new_state)
                
        return successors
    
    def print_moves_to(self):
        '''follows predecessor references back up the state-space search tree 
        in order to find and print the sequence of moves.'''
        #If self is the initial state (i.e. if its predecessor equals None),
        #print the string literal 'initial state' and then on the next line
        #the board associated with that state.
        if self.predecessor == None:
            print('initial state:')
            print(self.board)
            
        #Else:
        else:
            
            #Recursive call to print the moves of the predecessor state.
            self.predecessor.print_moves_to()
            
            #Print the move that led to self.
            print('move the blank ' + self.move)
            
            #Print the board associated with self.
            print(self.board)
            

if __name__ == '__main__':
    
    #__init__ test cases.
    b1 = Board('142358607')
    s1 = State(b1, None, 'init')
    print(s1)
    b2 = b1.copy()
    b2.move_blank('up')
    s2 = State(b2, s1, 'up')
    print(s2)
    b3 = b2.copy()
    b3.move_blank('up')
    s3 = State(b3, s2, 'up')
    print(s3)
    
    #is_goal test cases:
    s4 = State(Board('102345678'), None, 'init')
    print(s4.is_goal())
    s5 = State(Board('012345678'), s4, 'left')
    print(s5.is_goal())
    
    #generate_successors test cases.
    b4 = Board('142358607')
    print(b4)
    s6 = State(b4, None, 'init')
    print(s6)
    succ = s6.generate_successors()
    print(succ)
    
    #print_moves_to test case.
    b = Board('142305678') 
    s = State(b, None, 'init')   
    searcher = Searcher(-1)
    goal = searcher.find_solution(s)
    print(goal)
    print(goal.predecessor)
    print(goal.predecessor.predecessor)
    print(goal.predecessor.predecessor.predecessor)
    goal.print_moves_to()