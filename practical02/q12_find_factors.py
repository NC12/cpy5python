# Filename: q12_find_factors.py
# Name: Ng Cheryl
# Created: 20130203
# Modified: 20130203
# Description: Program that reads an integer and
# displays all its prime factors

# main
while True:

# declare an empty list
    factors = []

# prompt and get integer
    integer = int(input("Please enter a non-zero integer: "))

# check if integer is zero
    if integer == 0:
        print ("Error! This is not a non-zero integer!")

# initialise a variable to divide integer by,
# starting from smallest prime number: 2
    divisor = 2

# loop division until quotient of integer is 1
    while integer > 1:
        if integer % divisor == 0: # checks if divisor is a factor of integer
            factors.append(divisor) # adds factor to list
            integer = integer/divisor
            # assign quotient to variable integer and continue dividing

        else:
            divisor = divisor + 1
            # increase divisor by 1 and continue looping
        
# display result
    print ("Prime factors = " + str(factors))

# prompt for user to continue
    repeat = input("\nPress enter to continue, type end to exit: ")
    if repeat == "end":
        exit()
