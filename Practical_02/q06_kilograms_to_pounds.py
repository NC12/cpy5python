# Filename: q06_kilograms_to_pounds.py
# Name: Ng Cheryl
# Created: 20130203
# Modified: 20130203
# Description: Program that displays table converting kilograms to pounds
# from 1 kilogram to 10 kilograms

# main

# display heading
print ("Kilograms Pounds")

# loop 10 times
for i in range(1,11):
    # generate values for kilograms and corresponding value for pounds
    kilograms = i
    pounds = i*2.2 

    # format table such that values are in line
    print ("{0:<9} {1:.1f}".format(kilograms, pounds))
