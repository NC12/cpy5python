# Filename: q6_find_ascii_char.py
# Name: Ng Cheryl
# Created: 20130127
# Modified: 20130127
# Description: Program receives an ASCII code and displays its character

# main
while True: # to loop entire code
    while True: # to loop code if input is not an integer

# prompt and get ASCII code
        code = str(input("\nPlease enter ASCII code between 0 and 127: "))

# check if input is an integer
        try:
            code=int(code)
            break # to proceed to check if input is between 0 and 127
        
        except ValueError:
            print ("\nError!! This is not an integer")

#check if input is betwee 0 and 127        
    if int(code)<1 or int(code)>126:
        print ("\nError!! ASCII code is out of range!")
        
# convert ASCII code to character
    else:
        char = chr(int(code))
        
# display result
        print (char)
        

# prompt for user to continue
    repeat = input("\nPress enter to continue, type end to exit: ")
    if repeat == "end":
        exit()
