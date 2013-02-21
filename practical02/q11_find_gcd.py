# Filename: q11_find_gcd.py
# Name: Ng Cheryl
# Created: 20130203
# Modified: 20130203
# Description: Program find the greatest common divisor
# of two integers n1 and n2

# main
while True:

# prompt and get two non-zero integers from user
    n1 = int(input("Please enter a non-zero integer: "))
    n2 = int(input("Please enter another non-zero integer: "))

# check if n1 or n2 are zero
    if n1 == 0 or n2 == 0:
        print ("Error! This is not a non-zero integer!")
        
# find smaller of the two integers
    if n1 > n2:
        smaller = n2

    else:
        smaller = n1

# loop till greatest common divisor is found
    for x in range (smaller, 0, -1):
        if n1 % x == 0 and n2 % x == 0: # check if x is a divisor of n1 and n2
            print ("Greatest common divisor is " + str(x))
            break # to end loop when greatest common divisor is found
        
# prompt for user to continue
    repeat = input("\nPress enter to continue, type end to exit: ")
    if repeat == "end":
        exit()
        
    
