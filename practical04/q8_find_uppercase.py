# Filename: q8_find_uppercase.py
# Name: Ng Cheryl
# Created: 20130228
# Modified: 20130228
# Description: recursive function find_num_uppercase(str)
# to return the number of uppercase letters in a string str.
    
# define function
def find_num_uppercase(str):
    """ Function to return the number of uppercase letters in a string str"""
    # if all letters in str are lowercase
    if str == str.lower():
        return 0
    # terminating case
    elif 65 <= ord(str[0]) <= 90 and len(str) == 1:
        return 1
    # recursive case if lowercase letter found
    elif ord(str[0]) < 65 or ord(str[0]) > 90 and len(str) != 1:
        return 0 + find_num_uppercase(str[1:])
    # recursive case if uppercase letter found
    else:
        return 1 + find_num_uppercase(str[1:])


# main

# loop program
loop = True
while loop:
    
    # prompt user for string 
    string = str(input("Please enter a string of characters: "))
    
    # run function and display result
    if find_num_uppercase(string) == 1:
        print ("There is 1 uppercase letter!")
    else:
        print ("There are " + str(find_num_uppercase(string)) + " uppercase letters!")

    # prompt for user to continue
    cont = input("\nPress enter to continue, type end to exit: ")
    if cont == "end":
        loop = False # change value of loop to False to break loop

##>>> Output
##
##Please enter a string of characters: Good MorninG!
##There are 3 uppercase letters!
##
##Press enter to continue, type end to exit: 
