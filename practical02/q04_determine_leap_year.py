# Filename: q04_determine_leap_year.py
# Name: Ng Cheryl
# Created: 20130203
# Modified: 20130203
# Description: Program that prompts the user to enter a year
# and determines whether it is a leap year. 

# main
while True:

# prompt and get year
    year = int(input("Please enter a year: "))

# check if year is divisible by 4
    if year % 4 == 0:
        print (str(year) + " is a leap year!")

    else:
        print (str(year) + " is not a leap year!")

# prompt for user to continue
    repeat = input("\nPress enter to continue, type end to exit: ")
    if repeat == "end":
        exit()
    
