# Filename: q1_fahrenheit_to_celsius.py
# Name: Ng Cheryl
# Created: 20130121
# Modified: 20130127
# Description: Program to read Fahrenheit degree
# and convert it to Celsius

# main
while True:
    
# prompt and get Fahrenheit degree
    fahrenheit = float(input("\nPlease enter temperature in Fahrenheit:"))

# convert Fahrenheit degree into Celsius
    celsius = (5/9) * (fahrenheit - 32)

# display result
    print ("\nTemperature in Celsius = {0:.2f}".format(celsius) + "°C")

# prompt for user to continue
    repeat = input("\nPress enter to continue, type end to exit:")
    if repeat == "end":
        exit()
