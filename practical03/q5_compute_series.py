# Filename: q5_compute_series.py
# Name: Ng Cheryl
# Created: 20130222
# Modified: 20130222
# Description: function m_odd_series(i) to compute series
# and display the results for i from 1 to 19 in a table as a test program

# main
    
# define function
def m_odd_series(i):
    """ function to compute series """
    # initialise variable to store sum of series
    add = 0
    minus = 0
    for x in range(2*i-1, 0, -4): # skips fraction to be subtracted
        # accumulate sum of fractions to be added
        add = 1/x + add
        
    for x in range(2*i+1, 0, -4): # skips fraction to be added
        # accumulate sum of fractions to be subtracted
        minus = 1/x + minus
        
    # subtract alternate fractions from the sum of fractions added
    # and multiply by 4
    series = (add - minus)*4
    # format table such that values are in line
    print ("{0:<9} {1:.11f}".format(i, series))

    
# test program
# display heading
print ("{0} {1:>12}".format("i", "m(i)"))

# loop for odd numbers from 1 to 19
for a in range(1, 20, +2):
    # generate values for i and corresponding value of the sum of series
    m_odd_series(a)
    
# loop program
loop = True
while loop:
    # prompt and get integer from user
    integer = int(input("\nPlease enter an integer: "))
    # display heading
    print ("{0} {1:>12}".format("i", "m(i)"))
    # run function
    m_odd_series(integer)
    # prompt for user to continue
    cont = input("\nPress enter to continue, type end to exit: ")
    if cont == "end":
        loop = False # change value of loop to False to break loop


