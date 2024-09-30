#
# eight_puzzle.py (Final Project)
#
# Description: driver/test code for state-space search on Eight Puzzles.
# Date: 8/10/24
# Name: Benjamin Kim 
# email: benjt@bu.edu

from searcher import *
from timer import *

def create_searcher(algorithm, depth_limit = -1, heuristic = None):
    """ a function that creates and returns an appropriate
        searcher object, based on the specified inputs. 
        inputs:
          * algorithm - a string specifying which algorithm the searcher
              should implement
          * depth_limit - an optional parameter that can be used to
            specify a depth limit 
          * heuristic - an optional parameter that can be used to pass
            in a heuristic function
            
        Note: If an unknown value is passed in for the algorithm parameter,
        the function returns None.
    """
    searcher = None
    
    if algorithm == 'random':
        searcher = Searcher(depth_limit)
## You will uncommment the following lines as you implement
## other algorithms.
    elif algorithm == 'BFS':
        searcher = BFSearcher(depth_limit)
    elif algorithm == 'DFS':
        searcher = DFSearcher(depth_limit)
    elif algorithm == 'Greedy':
        searcher = GreedySearcher(depth_limit, heuristic)
    elif algorithm == 'A*':
        searcher = AStarSearcher(depth_limit, heuristic)
    else:  
        print('unknown algorithm:', algorithm)

    return searcher

def eight_puzzle(init_boardstr, algorithm, depth_limit = -1, heuristic = None):
    """ a driver function for solving Eight Puzzles using state-space search
        inputs:
          * init_boardstr - a string of digits specifying the configuration
            of the board in the initial state
          * algorithm - a string specifying which algorithm you want to use
          * depth_limit - an optional parameter that can be used to
            specify a depth limit 
          * heuristic - an optional parameter that can be used to pass
            in a heuristic function
    """
    init_board = Board(init_boardstr)
    init_state = State(init_board, None, 'init')

    searcher = create_searcher(algorithm, depth_limit, heuristic)
    if searcher == None:
        return

    soln = None
    timer = Timer(algorithm)
    timer.start()
    
    try:
        soln = searcher.find_solution(init_state)
    except KeyboardInterrupt:
        print('Search terminated.')

    timer.end()
    print(str(timer) + ', ', end='')
    print(searcher.num_tested, 'states')

    if soln == None:
        print('Failed to find a solution.')
    else:
        print('Found a solution requiring', soln.num_moves, 'moves.')
        show_steps = input('Show the moves (y/n)? ')
        if show_steps == 'y':
            soln.print_moves_to()

def process_file(filename, algorithm, depth_limit = -1, heuristic = None):
    '''solves each 8 puzzle in the file filename and reports on a variety of 
    statistics.'''
    #Filehandle that reads through the file
    file = open(filename, 'r')
    
    #Variables that we will use for reporting on our statistics later.
    num_solved = 0
    total_states = 0 
    total_moves = 0
    
    #For loop that iterates through each line/8 puzzle in the file.
    for line in file:
        
        #Increase the number of puzzles solved by 1 for each line.
        num_solved += 1
        
        #For each line, stripped_line will be the digit string that we will 
        #use to create our state and board objects. The variable state
        #will hold our state object.
        stripped_line = line.strip('\n')
        state = State(Board(stripped_line), None, 'init')
        
        #The specific searcher object that we need depending on our
        #algorithm, depth_limit and heuristic.
        searcher = create_searcher(algorithm, depth_limit, heuristic)
        
        #The following 5 lines of code gets the solution for the line
        #or retruns an error message if there isn't one.
        soln = None
        try:
            soln = searcher.find_solution(state)
        except KeyboardInterrupt:
            print('search terminated, ', end='')
            
        #For each line, add searcher.num_tested to total_states and 
        #soln.num_moves to total_moves so that we ultimately get 
        #the total number of states tested and moves performed after every
        #line.
        total_states += searcher.num_tested
        total_moves += soln.num_moves
        
        #For each line, report on the number of moves and states tested.
        print(stripped_line + ':', soln.num_moves, 'moves,', 
              searcher.num_tested, 'tested')
    
    #Lastly, report on the average number of moves and states tested.
    print('\nsolved', num_solved, 'puzzles\naverages:', total_moves / 
          num_solved, 'moves', total_states / num_solved, 'states tested')
    
if __name__ == '__main__':
    
    #eight_puzzle test cases.
    eight_puzzle('142358607', 'BFS', -1)
    
    #process_file('24_moves.txt', 'Greedy', -1, h1)
    #print('----------------------')
    #process_file('15_moves.txt', 'DFS', 20)