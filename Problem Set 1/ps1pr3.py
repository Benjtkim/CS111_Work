#
# File: ps1pr3.py - Problem Set 1, Problem 3
# Author name:
# Email:
# 
# Description: Indexing and slicing puzzles
#
# This is an individual-only problem that you must complete on your own.
#

#
# List puzzles
#

pi = [3, 1, 4, 1, 5, 9]
e = [2, 7, 1]

# Example puzzle (puzzle 0):
# Creating the list [2, 5, 9] from pi and e
answer0 = [e[0]] + pi[-2:] 

# Solve puzzles 1-4 here:
answer1 = e[0:2]

answer2 = [pi[4]] + pi[2:3] + pi[0:1]

answer3 = [pi[0]] + pi[4:5] + e[1:2]

answer4 = [e[2]] + e[0:1] + pi[0:5:2]


#
# String puzzles
#

b = 'boston'
u = 'university'
t = 'terriers'



# Example puzzle (puzzle 5)
# Creating the string 'bossy'
answer5 = b[:3] + t[-1] + u[-1]

# Solve puzzles 5-10 here:
answer6 = u[0:7] + t[1:2]

answer7 = t[2:3] + b[1:4] + t[5:7]

answer8 = b[0:2] + t[4:5] + b[2:4] + t[1:3] + b[1:2] + u[0:7:6]

answer9 = u[-1] + t[5:8:2] + u[-1] + t[5:8:2] + u[-1] + t[5:8:2]

answer10 = t[0:5:2] + b[2:4]

# test code below, do not modify!
if __name__ == '__main__':

    for x in ['answer0', 'answer1', 'answer2', 'answer3', 'answer4',
              'answer5', 'answer6', 'answer7', 'answer8', 'answer9',
              'answer10']:
        if x in dir():
            print(x + ' = ', eval(x))

    print(b[len(b) - 1: 0: -1])

