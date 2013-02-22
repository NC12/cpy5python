# Filename: q6_determine_prime.py
# Name: Ng Cheryl
# Created: 20130222
# Modified: 20130222
# Description: function is_prime(i) to determine whether
# an integer is a prime number and display
# every ten prime numbers in a row for the first thousand primes

# main
    
# define function
def is_prime(i):
    for divisor in range(i-1, 1, -1): # decreases divisor by 1 after every loop until 2
        if i % divisor == 0: # checks if divisor is a factor of integer
            prime = False 
        else:
            prime = True
    return (prime)
    print (prime)

    
# loop one hundred times
for x in range(0, 100):
    # initialise variable to store prime numbers in a row
    row = 0
    # loop 10 times
    for find in range(0, 10):
        i = 2
        while is_prime(i) == False:
            i = i + 1
            if is_prime(i): # if prime is True
                row = i + "     " + row
            
            print (row)
        

# loop for odd numbers from 1 to 19
for a in range(1, 20, +2):
    # generate values for i and corresponding value of the sum of series
    m_odd_series(a)
    
# loop program
loop = True
while loop:
    # prompt and get integer from user
    integer = int(input("Please enter an integer: "))
    # display heading
    print ("{0} {1:>12}".format("i", "m(i)"))
    # run function
    m_odd_series(integer)
    # prompt for user to continue
    cont = input("\nPress enter to continue, type end to exit: ")
    if cont == "end":
        loop = False # change value of loop to False to break loop

