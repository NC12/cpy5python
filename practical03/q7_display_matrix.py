# Filename: q7_display_matrix.py
# Name: Ng Cheryl
# Created: 20130222
# Modified: 20130222
# Description: funtction print_matrix(n) to display an n by n matrix,
# where n is a positive integer entered by the user.
# each element is generated randomly

# main
import random

# define function
def print_matrix(n):
    """ Function to generate matrix made out of random elements, 1 or 0"""
    # initialise variable to store rows in matrix
    rows = ""
    # loop to generate n rows
    for x in range(0, n): 
        # loop to generate n columns of either 1 or 0 in one row
        for x in range(0, n):
            # generate each element randomly and add it to row with a space in between
            rows = str(random.randint(0,1)) + " " + str(rows) 
        print (rows)
        rows = "" # reset value of rows to store a new row

# loop program
loop = True
while loop:
    # prompt and get integer from user
    integer = int(input("Please enter an integer: "))
    # run function
    print_matrix(integer)
    # prompt for user to continue
    cont = input("\nPress enter to continue, type end to exit: ")
    if cont == "end":
        loop = False # change value of loop to False to break loop

