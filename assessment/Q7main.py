#to start with i will import module sys to support other function like importing from the other file
import sys
#following instruction will import function from the file Q7functions
from Q7functions import left, right, both, grid

#this function will take 2 parameters and take action depending on the user input from the start of the program
def program(word, action):
    if action == "left":
        left(word)

    elif action =="right":
        right(word)

    elif action =="both":
        both(word)

    elif action =="grid":
        grid_size = int(input("what size of grid would you like to display?\n"))
        grid(word,grid_size)

    else:
        print("Invalid action. Please try again.")
        program()

#start of the program
#Program will request two user inputs to define the face they draw and the action they want to take
emoji = input("Please input the face using ascii:\n")
action = input("Please input the action: e.g. \"left\", \"right\", \"both\" or \"grid\"  \n")

#program will initate function program and assign two parameter accordingly to user input
program(emoji, action)
