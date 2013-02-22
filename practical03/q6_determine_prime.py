# Filename: q6_determine_prime.py
# Name: Ng Cheryl
# Created: 20130222
# Modified: 20130222
# Description: function is_prime(i) to determine whether
# an integer is a prime number and display
# every ten prime numbers in a row for the first thousand primes

# main
from math import sqrt

# define function
def is_prime(i):
    """ function to determine whether an integer is a prime number or not"""
    # solve easiest case
    if i == 1:
        return False
    for divisor in range (2, int(sqrt(i)+1)):
        # checks if divisor is a factor of integer
        if i % divisor == 0: 
            return False
    # if no divisors are found, i is a prime number
    return True

# initialise starting point of search
number = 2
# initialise variable to store number of primes found
total = 0
# initialise an empty list
primes = []
# find 1000 prime numbers, when 1000 primes are found, loop is broken
while total <= 1000:
    # if number is a prime, True is returned
    if is_prime(number) == True:
        
        # add number to list
        # format each number to take equal amount of space, 5 columns
        primes.append("{0:<5}".format(number)) 
        total = total + 1 # keeps track of number of primes found
    number = number + 1 # increase value of number by 1

# display heading
print("List of first 1000 prime numbers: ")
# loop 100 times
# increase value of n by 10, moves on to next row of numbers
for n in range(0, 1000, +10): # where n is the position of prime numbers in list
    print(primes[n], primes[n+1], primes[n+2], primes[n+3], primes[n+4], primes[n+5], primes[n+6], primes[n+7], primes[n+8], primes[n+9])
    
# loop program
loop = True
while loop:
    # prompt and get integer from user
    integer = int(input("\nPlease enter an integer to check if it is a prime number: "))
    # run function and display result
    if is_prime(integer) == True:
        print(str(integer) + " is a prime number!")
    else:
        print (str(integer) + " is not a prime number!")
    # prompt for user to continue
    cont = input("\nPress enter to continue, type end to exit: ")
    if cont == "end":
        loop = False # change value of loop to False to break loop

