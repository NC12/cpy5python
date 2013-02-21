# Filename: q07_miles_to_kilometres.py
# Name: Ng Cheryl
# Created: 20130203
# Modified: 20130203
# Description: Program that displays two tables side by side
# converting miles to kilometres and kilometres to miles

# main

# display heading
print ("Miles Kilometres Kilometres Miles")

# loop 10 times
for i in range(1,11):
    # generate values for miles and corresponding value for kilometres
    miles = i
    km = i*1.609
    km2 = (i+3)*5
    miles2 = km2/1.609

    # format table such that values are in line
    print ("{0:<5} {1:<10.3f} {2:<10} {3:.3f}".format(miles, km, km2, miles2))



