# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 15:53:25 2024

Name: Benjamin Kim
email: benjt@bu.edu
Description: Examples file for module 7. Includes a function and 2 code 
segments.
"""

def triple(vals):
    '''A function that modifies each value in a list by multiplying
    each value by 3.'''
    for i in range(len(vals)):
        vals[i] = vals[i] * 3
        
def main():
    '''This function will print [3, 6, 9] because lists are mutable
    and the triple function will have changed it.'''
    a = [1, 2, 3]
    triple(a)
    print(a)

#Nested loop. The runner variables both start at 0 and j iterates through
#each time i becomes a new number. 
for i in range(2):
    for j in range(3):
        print(i, j)

#2D list called table:
table = [[15, 8, 3, 16, 12, 7, 9, 5], 
         [6, 11, 9, 4, 1, 5, 8, 13],
         [17, 3, 5, 18, 10, 6, 7, 21],
         [8, 14, 13, 6, 13, 12, 8, 4],
         [1, 9, 5, 16, 20, 2, 3, 9]]

#Nested for loop that iterates through each individual value in the 2D list above.
#Works because each sublist has the same length of 8.
for r in range(len(table)):
    for c in range(len(table[0])):
        print(table[r][c])

if __name__ == '__main__':
    
    #Will print [3, 6, 9]
    main()
    
    #Will print 5 because table has 5 sublists.
    print(len(table))
    
    #Will print the second sublist within table because 
    #the second sublist has an index of 1.
    print(table[1])
    
    #Will print 8 because the 1st sublist has a length of 8.
    print(len(table[0]))
    
    #Will print 13 because [3][2] refers to the 3rd value
    #in the 4th sublist within table.
    print(table[3][2])


