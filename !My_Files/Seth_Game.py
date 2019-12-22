print("This is a RPG game for a Python 3")
print("Create your hero 'Knight' or 'Sorcerer'.")

hero_name = ""
hero_class = ""
hero_experience = 0
hero_weapon = (0,0)

def create_hero_name():
    print("Welcome hero. could you please tell me your name?\n")
    hero_name = str(input())
    create_hero_class()

def create_hero_class():
    print("It is a honor to meet you", hero_name, "what is your proffessions?")
    print("Are you a 'knight' or a 'sorcerer' ?")
    hero_class = str(input())
    if hero_class == "knight":
        print("Please take that sword", hero_name, "and slay or your enemies with its blade")
        print("You have received a long sword")
        hero_weapon = (5,3)
    elif hero_class == "sorcerer":
        print("Please take that wand", hero_name, "and slay or your enemies with magic")
        print("You have received a wand of light")
        hero_weapon = (6,1)
    else:
        print("Please come back when you are ready", hero_name)

create_hero_name()
print("hello")