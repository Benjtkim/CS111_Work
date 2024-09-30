#
# ps7pr2.py (Problem Set 7, Problem 2)
#
# Matrix operations
#
# Computer Science 111
# Date: 7/25/24
# Name: Benjamin Kim
# email: benjt@bu.edu
# Description: First set of problems dealing with matrices and matrix 
# operations.

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Enter a new matrix')
    print('(1) Negate the matrix')
    print('(2) Multiply a row by a constant')
    print('(3) Add one row to another')
    print('(4) Add a multiple of one row to another')
    print('(5) Transpose the matrix')
    print('(6) Quit')
    print()

def print_matrix(matrix):
    """ prints the specified matrix in rectangular form.
        input: matrix is a 2-D list numbers
    """
    ## You will revise this function. 
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if c == len(matrix[0]) - 1:
                print('%7.2f' % matrix[r][c], end='\n')
            else: 
                print('%7.2f' % matrix[r][c], end=' ')
       
def get_matrix():
    """ gets a new matrix from the user and returns it
    """
    matrix = eval(input('Enter a new 2-D list of numbers: '))
    return matrix

def negate_matrix(matrix):
    """ negates all of the elements in the specified matrix
        inputs: matrix is a rectangular 2-D list of numbers
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            matrix[r][c] *= -1
    # We don't need to return the matrix!
    # All changes to the matrix will still be there when the
    # function returns, because we received a copy of the
    # *reference* to the matrix used by main().

### Add your functions for options 2-5 here. ###

def mult_row(matrix, r, m):
    '''multiplies row r of the specified matrix by the specified 
    multiplier m.'''
    #For each value in the specified row, multiply that value by m.
    for c in range(len(matrix[r])):
        matrix[r][c] *= m

def add_row_into(matrix, rs, rd):
    ''' takes the specified 2-D list matrix and adds each element of row rs 
    (the source row) to the corresponding element of row rd 
    (the destination row).'''
    #For loop that iterates through the source row and the destination row
    #and adds the values togeether, only changing the destination row.
    for c in range(len(matrix[rs])):
        matrix[rd][c] = matrix[rd][c] + matrix[rs][c] 

def add_mult_row_into(matrix, m, rs, rd):
    '''takes the specified 2-D list matrix and adds each element of row rs 
    (the source row), multiplied by m, to the corresponding element of row rd 
    (the destination row).'''
    #Same logic as directly above except we multiply m to the number that's 
    #being added to the value in the destination row.
    for c in range(len(matrix[rs])):
        matrix[rd][c] = matrix[rd][c] + (matrix[rs][c] * m)

def transpose(matrix):
    '''takes the specified 2-D list matrix and creates and returns a new 2-D 
    list that is the transpose of matrix.'''
    #Empty list that will become the new matrix.
    new_matrix = []
    
    #This first line makes the loop run as many times as there are columns 
    #in matrix.
    for r in range(len(matrix[0])):
        #For the number of times there are columns in matrix, we will create 
        #then add a list of 0s to new_matrix. The number of 0s in each list
        #will be equal to the number of rows there are in matrix.
        row = [0] * len(matrix)
        new_matrix += [row]
    
    #For each value in the original matrix going right to left, the value 
    #in new_matrix going up to down will become said value. 
    for r in range(len(new_matrix)):
       for c in range(len(new_matrix[0])):
           new_matrix[r][c] = matrix[c][r]
            
    return new_matrix
        
def main():
    """ the main user-interaction loop
    """
    ## The default starting matrix.
    ## DO NOT CHANGE THESE LINES.
    matrix = [[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12]]

    while True:
        print()
        print_matrix(matrix)
        display_menu()
        choice = int(input('Enter your choice: '))

        if choice == 0:
            matrix = get_matrix()
        elif choice == 1:
            negate_matrix(matrix)

        ## add code to handle the other options here
        elif choice == 2:
            r = int(input('Enter the desired row: '))
            m = float(input('Enter the desired multiplier: '))
            mult_row(matrix, r, m)
        elif choice == 3:
            rs = int(input('Enter the desired source row: '))
            rd = int(input('Enter the desired destination row: '))
            add_row_into(matrix, rs, rd)
        elif choice == 4:
            m = float(input('Enter the desired multiplier: '))
            rs = int(input('Enter the desired source row: '))
            rd = int(input('Enter the desired destination row: '))
            add_mult_row_into(matrix, m, rs, rd)
        elif choice == 5:
            matrix = transpose(matrix)
        elif choice == 6:
            break
        else:
            print('Invalid choice. Try again.')

if __name__ == '__main__':
    
    main()