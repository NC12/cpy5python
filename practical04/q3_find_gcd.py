# Filename: q3_find_gcd.py
# Name: Ng Cheryl
# Created: 20130225
# Modified: 20130228
# Description: recursive function gcd(m, n) to find the GCD
    
# define function
def gcd(m, n):
    """ Function to find the greatest common divisior between two positive integers """
    # check if m or n are zero
    if m == 0 or n == 0:
        return "Error! This is NOT a non-zero integer!"
    # terminating case
    if m % n == 0:
        return n
    # recursive case
    else:
        return gcd(n, m % n)

# main

# loop program
loop = True
while loop:
    
    # prompt and get two non-zero integers from user
    int1 = int(input("Please enter a non-zero integer: "))
    int2 = int(input("Please enter another non-zero integer: "))
    print("Greatest common divisor of " + str(int1) + " and " + str(int2) + " is " + str(gcd(int1, int2)))
    
    # prompt for user to continue
    cont = input("\nPress enter to continue, type end to exit: ")
    if cont == "end":
        loop = False # change value of loop to False to break loop


##>>> Output
##Please enter a non-zero integer: 24
##Please enter another non-zero integer: 16
##Greatest common divisor of 24 and 16 is 8
##
##Press enter to continue, type end to exit: 
##Please enter a non-zero integer: 255
##Please enter another non-zero integer: 25
##Greatest common divisor of 255 and 25 is 5
##
##Press enter to continue, type end to exit: 



