# Filename: q1_display_reverse.py
# Name: Ng Cheryl
# Created: 20130218
# Updated: 20130221
# Description: function reverse_int(n)to display an integer in reverse order

# main
while True:
    
    # prompt user for integer
    integer = int(input("Please enter an integer: "))

    # define function
    def reverse_int(n):
        """ Function to reverse digits of an integer"""
        # initialise variable to store integer in reverse order
        reverse = 0
        # solve easiest case
        if n<10:
            print(n)

        # loop for the number of digits in the integer
        for i in range(0, len(str(n))):
            # accumulates sum of integer 
            reverse = reverse*10 + n%10
            # remove last digit of integer
            n = n//10
            
        # display integer
        print(reverse)

    # run function
    reverse_int(integer)

    # prompt for user to continue
    repeat = input("\nPress enter to continue, type end to exit:")
    if repeat == "end":
        exit()
    
