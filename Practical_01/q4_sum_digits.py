# Filename: q4_sum_digits.py
# Name: Ng Cheryl
# Created: 20130121
# Modified: 20130127
# Description: Program to read an integer between 0 and 1000
# and add all the digits in the integer

# main
while True:
    
# prompt and get number
    integer = int(input("\nPlease enter an integer between 0 and 1000: "))

# determine number of digits in integer
    no_of_digits = len (str(integer)) #invalid syntax at no_of_digits

# calculate sum of all digits
    if no_of_digits == 3:
           sum_of_digits = integer%10 + integer//100 + integer//10%10
    elif no_of_digits == 2:
           sum_of_digits = integer%10 + integer//10
    else:
           sum_of_digits = integer


# display result
    print (sum_of_digits)

# prompt for user to continue
    repeat = input("\nPress enter to continue, type end to exit:")
    if repeat == "end":
        exit()

