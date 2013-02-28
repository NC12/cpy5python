# Filename: q4_print_reverse.py
# Name: Ng Cheryl
# Created: 20130225
# Modified: 20130228
# Description: recursive function reverse_int(n) that reverses the digits of an integer n
    
# define function
def reverse_int(n):
    """ Function to reverse digits of an integer"""
    # terminating case
    if n<10:
        return n
    # recursive case
    else:
        # take last digit of 10 and multiply it by 10
        # to the power of the number of digits minus 1
        # such that it becomes the first digit
        return ((n % 10) * (10**(len(str(n))-1)) + reverse_int(n//10)) # remove last digit of integer


# main

# loop program
loop = True
while loop:
    
    # prompt user for integer
    integer = int(input("Please enter an integer: "))
    # run function
    print (reverse_int(integer))

    # prompt for user to continue
    cont = input("\nPress enter to continue, type end to exit: ")
    if cont == "end":
        loop = False # change value of loop to False to break loop

##>>> Output
##Please enter an integer: 12345
##54321
##
##Press enter to continue, type end to exit: 
