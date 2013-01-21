# Filename: q3_miles_to_kilometre.py
# Name: Ng Cheryl
# Created: 20130121
# Modified: 20130121
# Description: Program to read a distance in miles
# and converts it to kilometres

# main

# prompt to get distance in miles
distance = float(input("Please enter distance in miles:"))

# store value of a mile in kilometers
mile = 1.60934

# calculate distance in kilometres
distance_in_km = distance*mile

# display result to 3 decimal places
print("Distance in kilometers = {0:.3f}" .format(distance_in_km) + 'km')

              
