#
# File: ps1pr1.py - Problem Set 1, Problem 1
# Author name:
# Email:
# 
# Description: Computes the integers 0 through 4 using exactly 4 fours.
# 
# This is an individual-only problem that you must complete on your own.
#


zero = 4 + 4 - 4 - 4
one = 4 // 4 + 4 - 4
two = (4 // 4) + (4 // 4)
three = (4 + 4 + 4) // 4
four = 4 * (4 - 4) + 4

# Complete the rest of the program below.
for x in ['zero', 'one', 'two', 'three', 'four']:
    if x in dir():
        print(x + ' =', eval(x))





# test code below, do not modify!
#if __name__ == '__main__':
 
 #   for x in ['zero', 'one', 'two', 'three', 'four']:
  #      if x in dir():
   #         print(x + ' = ', eval(x))

