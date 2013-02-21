# Filename: q02_triangle.py
# Name: Ng Cheryl
# Created: 20130203
# Modified: 20130203
# Description: Program that reads three edges for a triangle
# and determines whether the input is valid
# and prints perimeter when valid and invalid if invalid

# main
while True:
    
# declare an empty list
    triside = []

# initialise variable to check for largest side
    largest = 0

# initialise sum
    perimeter = 0

# loop 3 times
    for i in range(0,3):
        # get sides from user and add to list
        triside.append(int(input("Please enter side " + str(i+1) + " of triangle: ")))
        # check for largest side
        if triside[i]>largest:
            largest = triside[i]

        # accumulate perimeter:
        perimeter = perimeter + triside[i]

# check if inputs are valid
    if perimeter - largest > largest:
        print ("Perimeter = " + str(perimeter)) # displays result if valid

    else:
        print ("Invalid triangle!") # display invalid if invalid
    
# prompt for user to continue
    repeat = input("\nPress enter to continue, type end to exit: ")
    if repeat == "end":
        exit()
    
        
    
    
    
    

