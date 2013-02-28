# Filename: q6_compute_sum.py
# Name: Ng Cheryl
# Created: 20130227
# Modified: 20130227
# Description: recursive function sum_digits(n)
# that computes the sum of the digits in an integer n

# define method
def sum_digits(n):
    """ function to compute the sum of the digits in an integer n """
    # terminating case
    if n < 10:
        return n
    # recursive case
    else:
        return n % 10 + sum_digits(n//10)
        

# main

# loop program
loop = True
while loop:
    # prompt and get integer from user
    integer = int(input("\nPlease enter an integer: "))
    # run function and display result
    print("Sum of digits is " + str(sum_digits(integer)))
    # prompt for user to continue
    cont = input("\nPress enter to continue, type end to exit: ")
    if cont == "end":
        loop = False # change value of loop to False to break loop

##>>> Output
##
##Please enter an integer: 234
##Sum of digits is 9
##
##Press enter to continue, type end to exit: 



