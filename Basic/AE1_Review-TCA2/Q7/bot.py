import sys

from functions import under, over, both, grid

def program(word, action):
    if action == "under":
        under(word)

    elif action =="over":
        over(word)

    elif action =="both":
        both(word)

    elif action =="grid":
        grid_size = int(input("what size of grid would you like to display?\n"))
        grid(word,grid_size)

    else:
        print("Invalid action. Please try again.")
        program()

word = input("Please input the word:\n")
action = input("Please input the action: e.g. \"under\", \"over\", \"both\" or \"grid\"  \n")
program(word, action)
