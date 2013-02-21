# Filename: q2_display_pattern.py
# Name: Ng Cheryl
# Created: 20130221
# Updated: 20130221
# Description: function display_pattern(n) to display
# a pattern of numbers in a right angle triangle

# main
while True:

    # prompt user and get integer
    integer = int(input("Please enter an integer: "))

    # define function
    def display_pattern(n):
        # solve easiest case
        if n==1:
            print (1)
        # initialise a variable to store values of numbers in triangle
        triangle = ""
        for i in range(1, n+1):
            if n<10:
                # account for the space a single digit number takes
                space = n*2
            elif 10<=n<100:
                # account for the space the first 9 digits take,
                # and the space the double digits take
                space = 9*2 + (n-9)*3
            elif 100<=n<1000:
                # account for the space the first 9 digits take,
                # and the space the first 90 double digits take
                # and the space the numbers with 3 digits take
                space = 9*2 + 90*3 + (n-99)*4
            triangle = str(i) + " " + str(triangle)
            
            # as i increases by 1, the length of triangle increases
            # subtract the length of triangle from number of spaces of the first line
            print(" "*(space - len(triangle)) + triangle) # display pattern

    # runs function
    display_pattern(integer)

    # prompt for user to continue
    repeat = input("\nPress enter to continue, type end to exit:")
    if repeat == "end":
        exit()
