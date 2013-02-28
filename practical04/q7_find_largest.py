# Filename: q7_find_largest.py
# Name: Ng Cheryl
# Created: 20130227
# Modified: 20130227
# Description: recursive function find_largest(alist)
# that returns the largest integer in an array alist.

# initialise variable to store largest integer
largest = 0

# define method
def find_largest(alist):
    """ function to return the largest integer in an array alist """
    # initialise variable to store largest integer
    # terminating case
    if len(alist) == 1:
        return alist[0]
    # recursive case for alist[0] more than the integers after position 0
    elif alist[0] > find_largest(alist[1:]):
        return alist[0]
    # recursive case for alist[0] less than the integers after position 0
    else:
        return find_largest(alist[1:])

# main

# loop program
loop = True
while loop:
    # prompt and get integer from user
    num_integers = int(input("\nHow many integers will you be entering? "))
    # declare an empty list
    numbers = []
    # loop as many times as integers to be entered
    for i in range(0,num_integers):
        numbers.append([int(input("\nEnter an integer: "))])
    
    # run function
    result = "Largest integer is " + str(find_largest(numbers))
    # remove [ and ] from the result, display result
    print (result.replace("[","").replace("]",""))
    # prompt for user to continue
    cont = input("\nPress enter to continue, type end to exit: ")
    if cont == "end":
        loop = False # change value of loop to False to break loop

##>>> Output
##        
##How many integers will you be entering? 5
##
##Enter an integer: 5
##
##Enter an integer: 1
##
##Enter an integer: 8
##
##Enter an integer: 7
##
##Enter an integer: 2
##Largest integer is 8
##
##Press enter to continue, type end to exit: 




