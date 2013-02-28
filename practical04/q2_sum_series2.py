# Filename: q2_sum_series2.py
# Name: Ng Cheryl
# Created: 20130225
# Modified: 20130225
# Description: recursive function sum_series2(i) to compute series of fractions
    
# define function
def sum_series2(i):
    """ function to compute series """
    # terminating case
    if i == 1:
        return 1/3
    # recursive case
    else:
        return i/(2*i+1) + sum_series2(i-1)

# main
    
# loop program
loop = True
while loop:
    # prompt and get integer from user
    integer = int(input("\nPlease enter an integer: "))
    # run function
    print(sum_series2(integer))
    # prompt for user to continue
    cont = input("\nPress enter to continue, type end to exit: ")
    if cont == "end":
        loop = False # change value of loop to False to break loop

##>>> Output
##
##Please enter an integer: 5
##2.060894660894661
##
##Press enter to continue, type end to exit: 

