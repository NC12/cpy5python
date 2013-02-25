# Filename: q3_find_gcd.py
# Name: Ng Cheryl
# Created: 20130222
# Modified: 20130222
# Description: function gcd(m, n) to return
# the greatest common divisor between two positive integers

# main

# define function
def gcd(m,n):
    """ Function to find the greatest common divisior between two positive integers """
    # check if m or n are zero
    if m == 0 or n == 0:
        print ("Error! This is not a non-zero integer!")
            
    # find smaller of the two integers
    if m > n:
        smaller = m

    else:
        smaller = n

    # loop till greatest common divisor is found
    for x in range (smaller, 0, -1):
        if m % x == 0 and n % x == 0: # check if x is a divisor of m and n
            print ("Greatest common divisor of " + str(m) + " and " + str(n) + " is " + str(x))
            break # to end loop when greatest common divisor is found
        
# test cases
gcd(24, 16)
gcd(255, 25)

# loop program
loop = True
while loop:
    
    # prompt and get two non-zero integers from user
    int1 = int(input("Please enter a non-zero integer: "))
    int2 = int(input("Please enter another non-zero integer: "))
    gcd(int1, int2)
    
    # prompt for user to continue
    cont = input("\nPress enter to continue, type end to exit: ")
    if cont == "end":
        loop = False # change value of loop to False to break loop
    
        

