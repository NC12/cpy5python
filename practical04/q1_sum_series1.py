# Filename: q1_sum_series1.py
# Name: Ng Cheryl
# Created: 20130225
# Modified: 20130301
# Description: recursive function sum_series1(i) to compute series of fractions
    
# define function
def sum_series1(i):
    """ function to compute series """
    # terminating case
    if i == 1:
        return 1
    elif i == 0:
        return "Error! Denominator cannot be 0!"
    # recursive case
    else:
        return 1/i + sum_series1(i-1)

# main
    
# loop program
loop = True
while loop:
    # prompt and get integer from user
    integer = int(input("\nPlease enter an integer: "))
    # run function
    print(sum_series1(integer))
    # prompt for user to continue
    cont = input("\nPress enter to continue, type end to exit: ")
    if cont == "end":
        loop = False # change value of loop to False to break loop

##>>> Output
##
##Please enter an integer: 3
##1.8333333333333333
##
##Press enter to continue, type end to exit: 
