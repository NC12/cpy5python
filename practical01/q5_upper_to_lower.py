# Filename: q5_upper_to_lower.py
# Name: Ng Cheryl
# Created: 20130127
# Modified: 20130127
# Description: Program converts an uppercase letter to a lowercase letter
# by making use of its ASCII value

# main
while True:

# prompt and get uppercase letter
    uppercase = str(input("\nPlease enter a single uppercase letter:"))

# check if input is a single uppercase letter and not a word or number
    if len(uppercase)!= 1 :
        print ("\nError!! There is more than one letter!")

    elif 97<=ord(uppercase)<=122:
        print ("\nError!! Letter is already in lowercase!")

    elif ord(uppercase)<65 or ord(uppercase)>90:
        print ("\nError!! This is not a letter!")

# convert uppercase letter to lowercase letter
# if input is already in lowercase, ASCII value will be out of range
# and lowercase will hence return nothing, leaving result to be a blank
    else:
        lowercase = chr (ord(uppercase) + 32)

# display result
        print (lowercase)

# prompt for user to continue
    repeat = input("\nPress enter to continue, type end to exit:")
    if repeat == "end":
        exit()


