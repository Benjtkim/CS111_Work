#
# ps8pr1.py - starter code for Problem Set 8, problem 1
# Date: 7/30/24
# Name: Benjamin Kim
# email: benjt@bu.edu
# Description: Using string methods to create new strings out of pre-existing
# ones.


s1 = 'Three little kittens lost their mittens'
s2 = 'Star light, star bright'


# count all occurrences of the letter T (both upper-case and lower-case) in s1, 
# and assign the count to the variable answer0
answer0 = s1.count('T') + s1.count('t')

# do your work here!
answer1 = s1.replace('tt', 'pp') 
answer2 = s2.split('r')
answer3 = s2.upper().replace('STAR', 'NIGHT')
answer4 = s1.lower().split('th')
answer5 = s2.replace('ight', 'ook').split(',')

# put any print statements/test code inside this controlled block:
if __name__ == '__main__':
    
    print('s1 =', s1)
    print('s2 =', s2)
    
    print('answer0 =', answer0)
    
    # optional: add your test code here
    print(s1.upper())   #prints s1 in all caps.
    print(s2.lower())   #prints s2 but with the first s in lower case.
    print(s2.count('s'))   #prints 1 (case sensitive).
    print(s2.lower().count('s'))   #prints 2 (since both s's are lower case).
    print(s1.count('tt'))   #prints 3.
    print(s1.split())   #prints a list where each element is each  word in s1.
    print(s1.split('t'))   #prints ['Three li', '', 'le ki', '', 'ens los', ' ', 'heir mi', '', 'ens'].
    print(s1.upper().split('T'))   #prints ['', 'HREE LI', '', 'LE KI', '', 'ENS LOS', ' ', 'HEIR MI', '', 'ENS'].
    print(s1.replace('th', 'f'))   #prints Three little kittens lost feir mittens.
    print(s1.lower().replace('th', 'f'))   #prints free little kittens lost feir mittens.
    print(s2.replace('r', 'x'))   #prints Stax light, stax bxight.
    print(s2.replace('ar', 'amp'))   #prints Stamp light, stamp bright.
    
    #Puzzle 1:
    print('answer1 =', answer1)
    
    #Puzzle 2:
    print('answer2 =', answer2)
    
    #Puzzle 3:
    print('answer3 =', answer3)
    
    #Puzzle 4:
    print('answer4 =', answer4)
    
    #Puzzle 5:
    print('answer5 =', answer5)

