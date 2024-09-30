#
# ps5pr4.py (Problem Set 5, Problem 4)
#
# Caesar cipher / decipher
#Name: Benjamin Kim
#email: benjt@bu.edu

# A template for a helper function called rot that we recommend writing
# as part of your work on the encipher function.
def rot(c, n):
    """Rotates a single character (c) forward by (n) spots in the alphabet."""
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)
    
    # Put the rest of your code for this function below.
    test1 ='a' <= c <= 'z'
    test2 ='A' <= c <= 'Z'
    tentative_result = chr(ord(c) + n)
    test3 = 'a' <= tentative_result <= 'z'
    test4 = 'A' <= tentative_result <= 'Z'
    
    if test1 == False and test2 == False:
        return c
    elif test3 == True and c.islower() == True:
        return tentative_result
    elif test4 == True and c.isupper() == True:
        return tentative_result
    else:
        return chr(ord(c) + n - 26)

#### Put your code for the encipher function below. ####
def encipher(s, n):
    '''Takes an arbitrary string (s) and a non-negative integer (n) between 0 
    and 25, and returns a new string in which the letters in s have been 
    “rotated” by n characters forward in the alphabet.'''
    if s == '':
        return ''
    else:
        rest = encipher(s[1:], n)
        return rot(s[0], n) + rest

# A helper function that could be useful when assessing
# the "Englishness" of a phrase.
# You do *NOT* need to modify this function.
def letter_probability(c):
    """ if c is the space character (' ') or an alphabetic character,
        returns c's monogram probability (for English);
        returns 1.0 for any other character.
        adapted from:
        http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    if c == ' ': return 0.1904
    if c == 'e' or c == 'E': return 0.1017
    if c == 't' or c == 'T': return 0.0737
    if c == 'a' or c == 'A': return 0.0661
    if c == 'o' or c == 'O': return 0.0610
    if c == 'i' or c == 'I': return 0.0562
    if c == 'n' or c == 'N': return 0.0557
    if c == 'h' or c == 'H': return 0.0542
    if c == 's' or c == 'S': return 0.0508
    if c == 'r' or c == 'R': return 0.0458
    if c == 'd' or c == 'D': return 0.0369
    if c == 'l' or c == 'L': return 0.0325
    if c == 'u' or c == 'U': return 0.0228
    if c == 'm' or c == 'M': return 0.0205
    if c == 'c' or c == 'C': return 0.0192
    if c == 'w' or c == 'W': return 0.0190
    if c == 'f' or c == 'F': return 0.0175
    if c == 'y' or c == 'Y': return 0.0165
    if c == 'g' or c == 'G': return 0.0161
    if c == 'p' or c == 'P': return 0.0131
    if c == 'b' or c == 'B': return 0.0115
    if c == 'v' or c == 'V': return 0.0088
    if c == 'k' or c == 'K': return 0.0066
    if c == 'x' or c == 'X': return 0.0014
    if c == 'j' or c == 'J': return 0.0008
    if c == 'q' or c == 'Q': return 0.0008
    if c == 'z' or c == 'Z': return 0.0005
    return 1.0

#### Put your code for the decipher function below. ####
def englishness_score(s):
    '''Computes the "Englishness" of string s.'''
    if s == '':
        return 0
    else:
        rest = englishness_score(s[1:])
        return rest + letter_probability(s[0])

def decipher(s):
    '''Deciphers the enciphered string, s.'''
    possible_decipherings = [encipher(s, x) for x in range(26)]
    possible_decipherings_with_scores = [[englishness_score(w), w] for w in possible_decipherings]
    best_pair = max(possible_decipherings_with_scores)
    return best_pair[1]

if __name__ == '__main__':
    
    #rot test cases.
    print(rot('a', 1))
    print(rot('y', 2))
    print(rot('Y', 3))
    print(rot('!', 4))
    print(rot('I', 25))
    
    #encipher test cases.
    print(encipher('xyza', 1))
    print(encipher('Caesar cipher? I prefer Caesar salad.', 25))
    
    #decipher test cases.
    print(decipher('Bzdrzq bhogdq? H oqdedq Bzdrzq rzkzc.'))
    print(decipher('Hu lkbjhapvu pz doha ylthpuz hmaly dl mvynla lclyfaopun dl ohcl slhyulk.'))
    
    