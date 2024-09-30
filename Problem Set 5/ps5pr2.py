#
# ps5pr2.py (Problem Set 5, Problem 2)
#
# List Comprehension
#
#Name: Benjamin Kim
#email: benjt@bu.edu

## INSTRUCTIONS: Uncomment these lines as you go, and test them at the console
#
lc1 = [x * 2 for x in range(5)]
#
#
#
#
words = ['hello', 'world', 'how', 'goes', 'it?']
lc2 = [w[1] for w in words]
#
#
#
lc3 = [2* (word[-1:0:-1] + word[0]) for word in ['hello', 'bye', 'no']]
#
#
#
#
lc4 = [x*x for x in range(1, 10) if x % 2 == 0]
#lc4 = [x*x if x % 2 == 0 else x for x in range(1, 10)]
#
#
#
#
lc5 = [True if c == 'b' or c == 'u' else False for c in 'bu be you']
#
#
#


## continue with writing functions below:
def powers_of(base, count):
    '''Takes a number (base) and a positive integer (count) and returns a 
    list containing the first count powers of base, beginning with the 0th 
    power.'''
    return [base**x for x in range(0, count)]

def shorter_than(n, wordlist):
    '''Takes an integer (n) and a list of strings (wordlist) and returns a 
    list consisting of all words from wordlist that are shorter than n.'''
    return [word for word in wordlist if len(word) < n]

if __name__ == '__main__':
    
    
    # test code below, do not modify!
    for x in ['lc1', 'lc2', 'lc3', 'lc4', 'lc5']:
        if x in dir():
            print(x + ' = ', eval(x))

    #powers_of test cases.
    print(powers_of(2, 5))
    print(powers_of(3, 4))
    
    #shorter_than test cases.
    print(shorter_than(4, ['only', 'recursion', 'on', 'the', 'brain']))  
    print(shorter_than(7, ['Boston', 'Chicago', 'Washington', 'Houston']))
    print(shorter_than(6, ['Boston', 'Chicago', 'Washington', 'Houston']))