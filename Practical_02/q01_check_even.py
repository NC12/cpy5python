# Filename: q01_check_even.py
# Name: Ng Cheryl
# Created: 20130130
# Modified: 20130203
# Description: Program to read an integer and
# checks whether it is even

# main
while True:
    
# prompt and get integer from user
    integer = int(input("Please enter an integer: "))

# check whether integer is even and display result
    if integer%2 == 0:
        print (str(integer) + " is even")

    else:
        print (str(integer) + " is odd")

# prompt for user to continue
    repeat = input("\nPress enter to continue, type end to exit: ")
    if repeat == "end":
        exit()

        
        
    
    
