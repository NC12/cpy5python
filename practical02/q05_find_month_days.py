# Filename: q05_find_month_days.py 
# Name: Ng Cheryl
# Created: 20130203
# Modified: 20130203
# Description: program that prompts the user to enter the month and year,
# and displays the number of days in the month.

# main
while True:

# declare a list of months
    months = ["January ", "February ", "March ", "April ", "May ", "June ",
              "July ", "August ", "September ", "October ",
              "November ", "December "]

# prompt and get year
    year = int(input("Please enter a year: "))

# prompt and get month x
    x = int(input("Please enter a month in number: "))

# check if year is a leap year
    if x == 2:
        if year % 4 == 0:
            print (months[x-1] + str(year) + " has 29 days.")

        else:
            print (months[x-1] + str(year) + " has 28 days.")

# match other months to corresponding number of days
    elif (x % 2 == 1 and 0<x<8) or (x % 2 == 0 and 7<x<13):
        print (months[x-1] + str(year) + " has 31 days.")

    else:
        print (months[x-1] + str(year) + " has 30 days.")

# prompt for user to continue
    repeat = input("\nPress enter to continue, type end to exit: ")
    if repeat == "end":
        exit()
    
