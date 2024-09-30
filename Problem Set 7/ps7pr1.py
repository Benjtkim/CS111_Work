#
# ps7pr1.py (Problem Set 7, Problem 1)
#
# 2-D Lists
#
# Computer Science 111
# Date: 7/25/24
# Name: Benjamin Kim
# email: benjt@bu.edu
# Description: First set of problems dealing with using nested loops to 
# manipulate 2D lists.


import random

def create_grid(height, width):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: height and width are non-negative integers
    """
    grid = []
    
    for r in range(height):
        row = [0] * width     # a row containing width 0s
        grid += [row]

    return grid

def print_grid(grid):
    """ prints the 2-D list specified by grid in 2-D form,
        with each row on its own line, and nothing between values.
        input: grid is a 2-D list. We assume that all of the cell
               values are integers between 0 and 9.
    """
    height = len(grid)
    width = len(grid[0])
    
    for r in range(height):
        for c in range(width):
            print(grid[r][c], end='')   # print nothing between values
        print()                         # at end of row, go to next line    

def diagonal_grid(height, width):
    """ creates and returns a height x width grid in which the cells
        on the diagonal are set to 1, and all other cells are 0.
        inputs: height and width are non-negative integers
    """
    grid = create_grid(height, width)   # initially all 0s

    for r in range(height):
        for c in range(width):
            if r == c:
                grid[r][c] = 1

    return grid

def inner_grid(height, width):
    '''creates and returns a 2-D list of height rows and width columns in 
    which the “inner” cells are all 1 and the cells on the outer border are 
    all 0.'''
    
    grid = create_grid(height, width)   # initially all 0s.
    
    #As long as r and c don't correspond to the first and last row/column, 
    #make every value a 1.
    for r in range(height):
        for c in range(width):
            if r != 0 and r != height - 1 and c != 0 and c != width - 1:
                grid[r][c] = 1
        
    return grid

def random_grid(height, width):
    '''creates and returns a 2-D list of height rows and width columns in 
    which the inner cells are randomly assigned either 0 or 1, but the cells 
    on the outer border are all 0.'''
    
    grid = create_grid(height, width)   #initially all 0s.
    
    #Same exact logic as the function above, except we're replacing 1 with 
    #random.choice([0, 1])
    for r in range(height):
        for c in range(width):
            if r != 0 and r != height - 1 and c != 0 and c != width - 1:
                grid[r][c] = random.choice([0, 1])

    return grid

def copy(grid):
    '''creates and returns a deep copy of grid.'''
    #Creates a new 2D list with the same dimensions as grid since len(grid)
    #represents the height and len(grid[0]) represents the width.
    copy_of_grid = create_grid(len(grid), len(grid[0]))
    
    #For loop that copies the individual values from the cells of grid into 
    #the cells of copy_of_grid.
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            copy_of_grid[r][c] = grid[r][c]
            
    return copy_of_grid

def invert(grid):
    '''takes an existing 2-D list of 0s and 1s and inverts it – changing all 0 
    values to 1, and changing all 1 values to 0.'''
    #For each value in each sublist in grid, if the value is 1, make it 0.
    #Otherwise (if it's 0), make it 1.
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                grid[r][c] = 0
            else:
                grid[r][c] = 1

if __name__ == '__main__':
    
    #Checking to ensure the given funcitons work.
    grid = diagonal_grid(6, 8)
    print_grid(grid)
    print('----------')
    
    #checking to ensure inner_grid works.
    grid = inner_grid(5, 5)
    print_grid(grid)
    print('----------')

    #checking to ensure random_grid works.
    grid = random_grid(4,5)
    print_grid(grid)
    print('----------')
    print('----------')
    
    #showcases how copying a list variable does not actually copy the list. 
    grid1 = create_grid(2, 2)
    grid2 = grid1      # copy grid1 into grid2
    print_grid(grid2)
    print('----------')
    grid1[0][0] = 1
    print_grid(grid1)
    print('----------')
    print_grid(grid2)
    print('----------')
    print('----------')
    
    #checking to ensure copy works.
    grid1 = diagonal_grid(3, 3)
    print_grid(grid1)
    print('----------')
    grid2 = copy(grid1)   # should get a deep copy of grid1
    print('----------')
    print_grid(grid2)
    print('----------')
    grid1[0][1] = 1
    print_grid(grid1)     # should see an extra 1 at [0][1]
    print('----------')
    print_grid(grid2)     # should not see an extra 1
    print('----------')
    print('----------')
    
    #checking to ensure invert works.
    grid = diagonal_grid(5, 5)
    print_grid(grid)
    print('----------')
    invert(grid)
    print_grid(grid)
    print('----------')
    print('----------')
    
    #another example to reinforce understanding of references.
    grid1 = inner_grid(5, 5)
    print_grid(grid1)
    print('----------')
    grid2 = grid1
    grid3 = grid1[:]
    invert(grid1)
    print_grid(grid1)
    print('----------')
    print_grid(grid2)   #should print inverted grid because grid2 is not a deep copy of grid1.
    print('----------')
    print_grid(grid3) #should print inverted grid because grid3 is not a deep copy of grid1.
    