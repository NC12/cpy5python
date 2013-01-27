# Filename: q3_miles_to_kilometre.py
# Name: Ng Cheryl
# Created: 20130121
# Modified: 20130127
# Description: Program to read a distance in miles
# and converts it to kilometres

# main
while True:
    
# prompt to get distance in miles
    distance = float(input("\nPlease enter distance in miles:"))

# store value of a mile in kilometers
    mile = 1.60934

# calculate distance in kilometres
    distance_in_km = distance*mile

# display result to 3 decimal places
    print("Distance in kilometers = {0:.3f}" .format(distance_in_km) + ' km')

# prompt for user to continue
    repeat = input("\nPress enter to continue, type end to exit:")
    if repeat == "end":
        exit()



              
