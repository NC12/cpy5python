# Filename: q8_convert_milliseconds.py
# Name: Ng Cheryl
# Created: 20130222
# Modified: 20130222
# Description: method convert_ms(n) to convert milliseconds to hours, minutes,
# and seconds, and return a string as hours:minutes:seconds.

# main

# define method
def convert_ms(n):
    """ method to convert milliseconds to hours, minutes and seconds"""
    hours = 60*60*1000
    minutes = 60*1000
    sec = 1000
    h_ms = n // hours # calculate number of hours
    n = n - h_ms*hours # subtract number of hours in milliseconds from n
    min_ms = n // minutes # calculate number of minutes
    n = n - min_ms*minutes # subtract number of hours in milliseconds from n
    s_ms = n //1000
    return (str(h_ms) + ":" + str(min_ms) + ":" + str(s_ms))

# loop program
loop = True
while loop:
    # prompt and get integer from user
    ms = int(input("Please enter milliseconds to be converted: "))
    # run function and display result
    print ("Milliseconds in hours:minutes:seconds is " + convert_ms(ms))
    # prompt for user to continue
    cont = input("\nPress enter to continue, type end to exit: ")
    if cont == "end":
        loop = False # change value of loop to False to break loop

