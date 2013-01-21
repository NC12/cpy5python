# Filename: q1_fahrenheit_to_celsius.py
# Name: Ng Cheryl
# Created: 20130121
# Modified: 20130121
# Description: Program to read Fahrenheit degree
# and convert it to Celsius

# main

# prompt and get Fahrenheit degree
Fahrenheit = float(input("Please enter temperature in Fahrenheit:"))

# convert Fahrenheit degree into Celsius
celsius = (5/9) * (Fahrenheit - 32)

# display result
print ("Temperature in Celsius = {0:.2f}".format(celsius) + "°C")
