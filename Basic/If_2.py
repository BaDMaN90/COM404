separator = ("____________________________________________________________________________________________")
print(separator)
print("| Hi, welcome to the program. I would like to know you better. Could you please tell me... ")
print(separator)
name = input("| what is your name? \n| ")
age =  int(input("| what is your age? \n| "))
print(separator)

print("| nice to meet you " + name + "!")
decision = str(input("| would you like to buy some alcohol?: \n| "))
print(separator)
answer = "yes"

if decision == answer:
    if age >= 25:
        print("| yay")
        
    elif age >= 18:
        print("| yay, can i please see your ID")
        
    else:
        print("| Meh, I cannot see you any alcohol")
        

    beer = ["stella", "kronnenbourg", "foster", "san miguel"]
    whiskey = ["Johnnie walker", "Jack daniels", "Jameson"]
    gin = ["bombay sapphire", "tanqueray", "mahon"]
    alcohol = input("| I have ... beer, whiskey or gin? \n| ")

    if alcohol == "beer":
        print(separator)
        print("| Beers i have are: .. ")
        print("|" , *beer, sep='\n| ')
        print(separator)
    elif alcohol == "whiskey":
        print(separator)
        print("| Whiskey i have are: .. ")
        print(*whiskey, sep='\n| ')
        print(separator)
    elif alcohol == "gin":  
        print(separator)
        print("| Gin's i have are: .. ")
        print(*gin, sep='\n| ')
        print(separator)
    else:
        print("sorry, I do not have that")
print("thank you, bye")
