def box(word):
    print("*" * (len(word) + 10))
    print("* Hello", word, "*")
    print("*" * (len(word) + 10))

def lower_case(word):
    print("Lower case function:", word.lower())

def upper_case(word):
    print("Upper case function:", word.upper())

def mirrored(word):
    reversed_phrase  = ""
    len_word = len(word)
    for x in range(0,len_word,1):
        reversed_phrase  = reversed_phrase + (word[len(word)-x-1])
    print("The phrase is: ", reversed_phrase)

def repeat(word):
    no_of_repeat = int(input("how many time repeat that word?\n"))
    if no_of_repeat >= 1:
        while no_of_repeat != 0:
            print(word)
            no_of_repeat -= 1
    else:
        print("error.")

def user_input():
    word = input("please enter the word. \n")
    function = input("what function would you like to use? 'box', 'lower case', 'upper case', 'mirrored', 'repeat'\n")
    if function == "box":
        box(word)
    elif function == "lower case":
        lower_case(word)
    elif function == "upper case":
        upper_case(word)
    elif function == "mirrored":
        mirrored(word)
    elif function == "repeat":
        repeat(word)
    else:
        print("Function unknown.")

user_input()