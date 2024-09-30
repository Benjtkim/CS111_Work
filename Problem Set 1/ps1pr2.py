#
# File: ps1pr2.py - Problem Set 1, Problem 2
# Author name:
# Email:
# 
# Description: Making change from a dollar
#
# This is an individual-only problem that you must complete on your own.
#

# To make the autograder script work, you will need to follow these constraints:
# * You must have variables named price, change, quarters, dimes, nickels,
#   and pennies. You may include any additional variables you choose.
# * In your finished code, put all print statements at the bottom 
#   (as indicated by the comment).
#   You may use print statements elsewhere in your code while you are developing
#   and testing, but you should comment out those print statements before submission. 



# once you have a working solution, you should change this line to test other 
# starting values, e.g., 68 cents, 69 cents, etc. to ensure that your calculations 
# work for each value.
price = 59
change = 100 - price


# do all of your computations here:
quarters = change // 25
dimes = ((change - 25 * quarters)) // 10
nickels = (change - (25 * quarters) - (10 * dimes)) // 5
pennies = (change - (25 * quarters) - (10 * dimes) - (5 * nickels)) 

print(change, quarters, dimes, nickels, pennies)

# put all print statements in this section:
print("The price of your item is " + str(price) + " cents, and your change is " + str(change) + " cents.\nHere's the change that uses the fewest coins:")
print("pennies: " + str(pennies))
print("nickels: " + str(nickels))
print("dimes: " + str(dimes))
print("quarters: " + str(quarters))


    
    
