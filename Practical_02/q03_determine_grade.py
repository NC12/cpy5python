# Filename: q03_determine_grade.py
# Name: Ng Cheryl
# Created: 20130203
# Modified: 20130203
# Description: Program that prompts user to enter a score
# from 0 to 100 inclusive and prints the grade

# main
while True:

# prompt and get user to enter score
    score = int(input("Please enter a score between 0 and 100: "))

# match score to grading system
    if 70<=score<=100:
        print ("A")

    elif 60<=score<=69:
        print ("B")

    elif 55<=score<=59:
        print ("C")

    elif 50<=score<=54:
        print ("D")

    elif 45<=score<=49:
        print ("E")

    elif 35<=score<=44:
        print ("S")

    elif 0<=score<=34:
        print ("U")

    else: # if score is not in range, score is invalid
        print ("Invalid! Score must be within 0 - 100.")

# prompt for user to continue
    repeat = input("\nPress enter to continue, type end to exit: ")
    if repeat == "end":
        exit()
    
