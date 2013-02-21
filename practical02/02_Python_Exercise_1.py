# Write a program to prompt the user for x positive
# integers, one at a time.
# Compute the sum of all x integers entered.

# Use a list.

# declare an empty list
numlist=[]

# get number of times (x) from user
x = int(input("How many integers do you want to enter?"))

# initialize sum
total = 0

# loop x times
for i in range(0,x):
    # get positive integer from user
    numlist.append(int(input("Please enter a postive integer: ")))#adds to list
    # accumulate sum
    total = total + numlist[i]
    print (total)


    


