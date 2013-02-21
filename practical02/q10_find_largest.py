# Filename: q10_find_largest.py
# Name: Ng Cheryl
# Created: 20130203
# Modified: 20130203
# Description: Program to find the largest integer n
# such that n**3 is less than 12,000.

# main

# initialise variable n
n=0

# loop till largest integer is found
while True:
    cube = n**3

    # check if cube of n is more than 12000
    if cube > 12000:
        n = n-1 # takes value of n from previous loop
        print ("The largest integer whose cube is lesser than 12,000 is "
               + str(n))
        break # break loop when largest integer is found

    else:
        n = n+1 # increases value of n by 1 and continues the loop
        
        
    
