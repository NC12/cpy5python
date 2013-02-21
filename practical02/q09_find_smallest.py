# Filename: q09_find_smallest.py
# Name: Ng Cheryl
# Created: 20130203
# Modified: 20130203
# Description: Program to find the smallest integer n
# such that n**2 is greater than 12,000

# main

# initialise variable n
n=0

# loop till smallest integer is found
while True:
    square = n**2

    # check if square of n is lesser than 12000
    if square < 12000:
        n = n+1 # increase value of n by 1 and continue the loop

    else: 
        print ("The smallest integer whose square is greater than 12,000 is "
               + str(n))
        break # break loop when square of n is more than 12000
    
