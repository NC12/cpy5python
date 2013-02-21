# Filename: q2_calc_cylinder_volume.py
# Name: Ng Cheryl
# Created: 20130121
# Modified: 20130127
# Description: Program to read the radius and length of a cylinder
# and computes its volume

# main
while True:
    
# prompt and ask if calculating in m or cm
    confirm = input("\nAre you calculating in m or cm? ")

# assign output unit
    if confirm == "m":
        unit = " cubic meters"
    else:
        unit = " cubic centimeters"

# prompt and get radius
    radius = float(input("\nPlease enter radius of cylinder in indicated unit:"))

# promt and get length
    length = float(input("Please enter length of cylinder in indicated unit:"))

# import pi
    from math import pi

# calculate area
    area = radius * radius * pi

# calculate volume
    volume = area * length

# display result
    print ("\nVolume = {0:.2f}".format(volume) + unit)

# prompt for user to continue
    repeat = input("\nPress enter to continue, type end to exit:")
    if repeat == "end":
        exit()
