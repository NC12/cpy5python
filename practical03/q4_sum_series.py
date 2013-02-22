# Filename: q4_sum_series.py
# Name: Ng Cheryl
# Created: 20130222
# Modified: 20130222
# Description: function m_series(i) to compute series
# and display the results for i from 1 to 20 in a table as a test program

# main
    
# define function
def m_series(i):
    """ function to compute series """
    # initialise variable to store sum of series
    series = 0
    for x in range(i, 0, -1):
        # accumulate sum
        series = x/(x+1) + series
    # format table such that values are in line
    print ("{0:<9} {1:.4f}".format(i, series))

    
# test program
# display heading
print ("{0} {1:>12}".format("i", "m(i)"))

# loop 20 times
for a in range(1,21):
    # generate values for i and corresponding value of the sum of series
    m_series(a)
    
# loop program
loop = True
while loop:
    # prompt and get integer from user
    integer = int(input("\nPlease enter a non-zero integer: "))
    # display heading
    print ("{0} {1:>12}".format("i", "m(i)"))
    # run function
    m_series(integer)
    # prompt for user to continue
    cont = input("\nPress enter to continue, type end to exit: ")
    if cont == "end":
        loop = False # change value of loop to False to break loop



