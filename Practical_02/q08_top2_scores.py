# Filename: q08_top2_scores.py
# Name: Ng Cheryl
# Created: 20130203
# Modified: 20130203
# Description: Program prompts the user to enter the number of students
# and each student's name and score, and displays the
# student with the highest score
# and the student with the second-highest score.

# main

# declare an empty list
students = []

# prompt and get number of students x
x = int(input("Please enter the number of students: "))

# intialise variable to check for highest and 2nd highest score
highest = 0
highest2 = 0

# loop x times
for i in range(0,x):
    students.append([input("\nEnter the student's name:")
                     , int(input("Enter the student's score:"))])
    
# check for student with highest score
    if students[i][1]> highest:
        highest = students[i][1]
        first = i # remember position of student with highest score

# display result
print ("\nStudent with highest score: " + str(students[first]))

# change value of highest score to 0 
students[first][1] = 0 

# search for 2nd highest score
for i in range(0,x):
    if students[i][1]> highest2:
        highest2 = students[i][1]
        second = i # remember position of student with 2nd highest score

# display result
print ("Student with 2nd highest score: " + str(students[second]))

