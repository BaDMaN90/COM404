separator = ("____________________________________________________________________________________________")
import time
basket = []
xrange = ""

def purchase_request():

    decision = str(input("| would you like to buy some alcohol?: \'yes\' or \'no\' \n| "))
    print(separator)
    answer = "yes"
    if decision == answer:
        alcohol_function()
    else:    
        print("| Oh, ok")
        time.sleep(2)

def alcohol_function():
    
    beer = ["stella", "kronnenbourg", "foster", "san miguel"]
    whiskey = ["Johnnie walker", "Jack daniels", "Jameson"]
    gin = ["bombay sapphire", "tanqueray", "mahon"]
    print("| I have many... beer's, whiskey's and gin's. Would you like to browse any?")
    alcohol = input("| Please type 'beer' or 'whiskey' or 'gin' \n| ")

    if alcohol == "beer":
        print(separator)
        print("| Beers i have are:")
        print("|" , *beer, sep='\n|> ')
        print(separator)
        alcohol_purchase(beer)
    elif alcohol == "whiskey":
        print(separator)
        print("| Whiskey i have are:")
        print("|" ,*whiskey, sep='\n|> ')
        print(separator)
        alcohol_purchase(whiskey)
    elif alcohol == "gin":  
        print(separator)
        print("| Gin's i have are:")
        print("|" ,*gin, sep='\n|> ')
        print(separator)
        alcohol_purchase(gin)
    else:
        print("sorry, I do not have that")

def alcohol_purchase(alcohol_type):

    item = input("| Please choose your item: \n|")
    if item in alcohol_type:
        basket.append('\n|>' + item)
    else:
        print("| I am sorry, I do not have that.")
        time.sleep(1)
    print(separator)
    decision = str(input("| would you like to buy more alcohol? \'yes\' or \'no\' \n| "))
    print(separator)
    answer = "yes"
    if decision == answer:
        alcohol_function()
    else:
        time.sleep(1)
        print("| your total shopping is: ", *basket)
        print(separator)
        time.sleep(2)

def shop():
    for x in range(90):
        print("\n")
    print(separator)
    print("| Hi, welcome to the alcohol shopping program. I need to verify some information. \n| Could you please tell me... ")
    print(separator)
    name = input("| what is your name? \n| ")
    print(separator)
    time.sleep(1)
    print("| nice to meet you " + name + "!")
    print(separator)
    time.sleep(1)
    age =  int(input("| what is your age? \n| "))
    print(separator)



    if age >= 25:
        print("| Yay, you are allowed to make a purchase")
        purchase_request()
            
    elif age >= 18:
        print("| yay, can i please see your ID before i will allow to make a purchase")
        time.sleep(1)
        print("| scanning ID...")
        time.sleep(3)
        print("| Age verified, thank you.")
        print(separator)
        time.sleep(1)
        purchase_request()
    else:
        print("| Sorry, I cannot sell you any alcohol")

    print("| Thank you, bye")
    time.sleep(3)
    shop()
shop()