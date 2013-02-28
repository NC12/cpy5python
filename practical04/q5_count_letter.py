# Filename: q5_count_letter.py
# Name: Ng Cheryl
# Created: 20130225
# Modified: 20130228
# Description: recursive function count_letter(str, ch) that finds the
# number of occurrences of a specified letter ch in a string str
    
# define function
def count_letter(str, ch):
    """ Function to find the number of occurrences
    of a specified letter ch in a string str"""
    # find the first occurrence of ch and assign it to variable start
    start = str.find(ch)
    # if letter not found
    if start == -1:
        return 0
    # terminating case
    if start != -1 and str.find(ch, start + 1) == -1:
        return 1
    # recursive case
    else:
        return 1 + count_letter(str[start+1:], ch)


# main

# loop program
loop = True
while loop:
    
    # prompt user for string 
    string = str(input("Please enter a string of characters: "))
    # prompt user for character
    char = str(input("Please enter the character you want to find (case-sensitive): "))
    
    # run function and display result
    print (char + " occurs " + str(count_letter(string, char)) + " time(s)!")

    # prompt for user to continue
    cont = input("\nPress enter to continue, type end to exit: ")
    if cont == "end":
        loop = False # change value of loop to False to break loop

##>>> Output
##Please enter a string of characters: Welcome
##Please enter the character you want to find: e
##e occurs 2 times!
##
##Press enter to continue, type end to exit: 
##
